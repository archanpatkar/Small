class Small:

    def __init__(self):
        pass;

    def parse(self,string):
        return list(filter(lambda char: char != " " and char != "\n", string));

    def execute(self,code):
        code = self.parse(code);
        counter = 0;
        for operation in code :
            if(counter >= 127):
                counter = 0;
            if(operation == "+"):
                counter += 1;
            elif(operation == "."):
                print(chr(counter), end='');
            elif(operation == "-"):
                counter -= 1;

    def executeFromFile(self,filepath):
        if(filepath != None):
            file = open(filepath, 'r');
            code = file.readlines();
            self.execute("".join(code));
