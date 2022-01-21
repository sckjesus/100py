
def backwards(statement):
    a=len(str(statement))+str(statement).count(" ")
    print(statement[::-1])
a=input("Say a word: ")
backwards(a)