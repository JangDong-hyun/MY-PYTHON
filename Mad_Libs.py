# Mad Libs


import re




text = """Giraffes have aroused
the curiosity of __PLURAL_NOUN__
since earliest times. The
giraffe is the tallest of all
living__PLURAL_NOUN__ . but
scientists are unable to
explain how i got its long
__PART_OF_BODY__. The
giraffe's tremendous height ,
which might reach __NUMER__
__PLURAL_NOUN__ , comes from
it legs and  __BODYPART__."""



def mad_libs(mls):
    """
    매개변수 mls: 사용자가 맞춰야 할 단어의 힌트는 밑줄 두개 사이에 쓴다.
    힌트에 밑줄 두개가  들어 있으면 안된다.
    """

    hints = re.findall("__.*?__" , mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word , new)

        print('\n')
        mls = mls.replace("\n" , "")
        print(mls)
    else:
        print("invalid mls")



mad_libs(text)
