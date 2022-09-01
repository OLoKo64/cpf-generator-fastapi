from typing import List


class Cpf:
    def __init__(self, cpf: str):
        self.cpf = cpf
        self.formatted_cpf = self.formatted_cpf()
        self.state = self.cpf_state()

    def get_all_cpf(self):
        return {
            "cpf": self.cpf,
            "formatted-cpf": self.formatted_cpf,
            "state": self.state
        }

    def unformatted_cpf(self) -> str:
        return self.cpf

    def formatted_cpf(self) -> str:
        formatted_cpf = ''.join([''.join(self.cpf[:3]), '.', ''.join(
            self.cpf[3:6]), '.', ''.join(self.cpf[6:9]), '-', ''.join(self.cpf[9:])])
        return formatted_cpf

    def cpf_state(self) -> List[str]:
        state_code = self.cpf[8:9]
        if state_code == '0':
            return ['RS']
        elif state_code == '1':
            return ['DF', 'GO', 'MT', 'MS', 'TO']
        elif state_code == '2':
            return ['AC', 'AM', 'AP', 'PA', 'RO', 'RR']
        elif state_code == '3':
            return ['CE', 'MA', 'PI']
        elif state_code == '4':
            return ['AL', 'PB', 'PE', 'RN']
        elif state_code == '5':
            return ['BA', 'SE']
        elif state_code == '6':
            return ['MG']
        elif state_code == '7':
            return ['ES', 'RJ']
        elif state_code == '8':
            return ['SP']
        elif state_code == '9':
            return ['PR', 'SC']
        else:
            raise Exception('Invalid CPF')
