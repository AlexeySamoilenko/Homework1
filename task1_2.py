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
        #assert Version(version_2) > Version(version_1), 'ge failed'
        assert Version(version_2) != Version(version_1), 'neq failed'
        
    
def gt(_, __):
        if _[:min(len(_), len(__))] == __[:min(len(_), len(__))] and len(_) == 3 and len(_) < len(__):
            return True
        elif _[:min(len(_), len(__))] == __[:min(len(_), len(__))] and len(__) == 3 and len(_) > len(__):
            return False
        if _[:min(len(_), len(__))] == __[:min(len(_), len(__))] and len(_) > len(__):
            return True
        elif _[:min(len(_), len(__))] == __[:min(len(_), len(__))] and len(_) < len(__):
            return False
        
        for i in range(min(len(_),len(__))):
            if re.match(r'(\d+\D+)|(\D+\d+)', _[i]+__[i]) and _[i] != __[i]:
                if re.findall(r'\d+', _[i]) < re.findall(r'\d+', __[i]):
                    return False
                elif re.findall(r'\D+', _[i]) > re.findall(r'\D+', __[i]):
                    print(re.findall(r'\D+', _[i]))
                    return True
            
            if _[i] < __[i]:
                print(5,_[i],__[i])
                return False

def split_str(_,__):
    #_ = _.get_version()
    _= _.replace(".", " ").replace("-", " ").split()
    #__ =__.get_version()
    __=__.replace(".", " ").replace("-", " ").split()     
    return gt(_, __)

if __name__ == "__main__":
    main()
