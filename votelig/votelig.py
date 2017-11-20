import argparse, types

class Votelig:
    '''
    Verifies voter eligibility based on age. Eligible if voter's age >= minimum voter age
    Default minimum voter age = 18 can be overridden
    Accepts positive integer age inputs.
    Converts string and unicode datatypes if they contain integers. Rejects all other datatypes.
    '''

    def __init__(self, min_voter_age = 18):
        self.min_voter_age = self.validate_age(min_voter_age, "Minimum voter age")
        return

    def is_eligible(self, age):
        age = self.validate_age(age, "Voter age")
        return True if (age >= self.min_voter_age) else False


    def validate_age(self, input_age, field):
        errormsg = "Invalid input {0}. {1} must be positive integer".format(input_age, field)

        if type(input_age) not in [types.StringTypes, types.IntType]: # float,boolean,long etc.
            raise Exception(errormsg)

        try: # Converts string and unicode to integer if possible

            age = int(input_age)
            if age >= 0 :
                return age
            else:
                raise Exception(errormsg)

        except: # Failed to convert. Contains alpha or special characters
            raise Exception(errormsg)

def main_arg_process(args):
    votelig = Votelig(args.min_age)
    print votelig.is_eligible(args.voter_age)

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Verify voter eligibility based on age.')
    parser.add_argument('voter_age', type=int,  metavar='N',help='Voter age')
    parser.add_argument('--min-age',type=int, help='Minimum voter age')
    args=parser.parse_args()
    main_arg_process(args)


