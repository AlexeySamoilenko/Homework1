from functools import total_ordering
import re

@total_ordering
class Version:
    def __init__(self, version: str):
        self.version = version
        
    def get_version(self):
        return self.version
    
    def __gt__(self, other):
        return split_str(self.version, other.version)
    
    def __lt__(self, other):
        return False if split_str(self.version, other.version) == True else True
    
    def __eq__(self, other):
        return self.version == other.version


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1b', '1.0.10-alpha.beta'),
        ('1.0.0-rc.1', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), 'le failed'
        assert Version(version_2) > Version(version_1), 'ge failed'
        assert Version(version_2) != Version(version_1), 'neq failed'


def split_str(version_1,version_2):
    version_1 = version_1.replace(".", " ").replace("-", " ").split()
    version_2 = version_2.replace(".", " ").replace("-", " ").split()     
    return gt(version_1,version_2)
    
def gt(version_1:list, version_2:list) -> bool:
    
    min_len_list = min(len(version_1), len(version_2))
        
    if version_1[:min_len_list] == version_2[:min_len_list] and len(version_1) == 3 and len(version_1) < len(version_2):
        return True
    elif version_1[:min_len_list] == version_2[:min_len_list] and len(version_2) == 3 and len(version_1) > len(version_2):
        return False
    if version_1[:min_len_list] == version_2[:min_len_list] and len(version_1) > len(version_2):
        return True
    elif version_1[:min_len_list] == version_2[:min_len_list] and len(version_1) < len(version_2):
        return False
        
    for i in range(min_len_list):
        if re.findall(r'(\d+\D+)|(\D+\d+)', version_1[i] + version_2[i]) and version_1[i] != version_2[i]:
            if re.findall(r'\d+', version_1[i]) < re.findall(r'\d+', version_2[i]):
                return False
            elif re.findall(r'\d+', version_1[i]) > re.findall(r'\d+', version_2[i]):
                return True
            elif re.findall(r'\D+', version_1[i]) > re.findall(r'\D+', version_2[i]):
                return True
        
        if version_1[i] > version_2[i]:
            return True
        elif version_1[i] < version_2[i]:
            return False



if __name__ == "__main__":
main()

