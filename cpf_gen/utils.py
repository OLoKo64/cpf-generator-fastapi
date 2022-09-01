from typing import List
import random
import string
import functools
from cpf_gen.cpf import Cpf
from fastapi import HTTPException


def generate_cpf(state: int = None) -> str:
    cpf_seed = random_seed()

    if state is not None:
        if state < 0 or state > 9:
            return HTTPException(status_code=406, detail="Invalid CPF, state code must be a number between 0 and 9")
        cpf_seed[8] = state

    sum_of_elements = functools.reduce(
        lambda a, b: a + b, map(lambda x: x[1] * (10 - x[0]), enumerate(cpf_seed)))
    verifier_one = calculate_verifier(sum_of_elements)
    cpf_seed_with_verifier_one = cpf_seed[1:] + [verifier_one]

    sum_of_elements = functools.reduce(
        lambda a, b: a + b, map(lambda x: x[1] * (10 - x[0]), enumerate(cpf_seed_with_verifier_one)))
    verifier_two = calculate_verifier(sum_of_elements)
    cpf = Cpf(''.join(map(str, cpf_seed + [verifier_one, verifier_two])))

    return cpf.get_all_cpf()


def random_seed() -> str:
    # return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(9))
    return [int(random.choice(string.digits)) for _ in range(9)]


def calculate_verifier(n1: int) -> int:
    n2 = n1 % 11
    return 0 if n2 < 2 else 11 - n2
