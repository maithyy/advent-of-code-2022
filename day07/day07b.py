class Directory:
    def __init__(self, dir_name, previous_dir):
        self.name = dir_name
        self.prev = previous_dir
        self.files = []
    
    def get_name(self):
        return self.name

    def get_prev(self):
        return self.prev
    
    def get_files(self):
        return self.files

    def add_file(self, my_file):
        self.files.append(my_file)

    def get_dir(self, dir_name):
        for obj in self.files:
            if type(obj) == Directory and obj.get_name() == dir_name:
                return obj
        print("get dir gone wrong!")

class File:
    def __init__(self, file_name, file_size):
        self.name = file_name
        self.size = file_size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size


def if_command(line):
    if line[0] != "$":
        return False
    return True, line.split()[1]


def create_directories():
    with open('input.txt') as f:
        base_dir = Directory("/", None)
        current_dir = None
        line = f.readline()
        while True:
            command = line.rstrip().split()[1]
            if command == "cd":
                directory = line.rstrip().split()[2]
                if directory == "..":
                    current_dir = current_dir.get_prev()
                elif directory == "/":
                    current_dir = base_dir
                else:
                    current_dir = current_dir.get_dir(directory)
                line = f.readline()
            elif command == "ls":
                while "$" not in (line:= f.readline().rstrip()):
                    if not line:
                        return base_dir
                    if "dir" in line:
                        my_file = Directory(line.split()[1], current_dir)
                    else:
                        my_file = File(line.split()[1], int(line.split()[0]))
                    current_dir.add_file(my_file)

def recursive_print(base_dir):
    for dir in base_dir.get_files():
        if type(dir) == Directory:
            print("new dir", dir.get_name())
            recursive_print(dir)
        else:
            print("file:", dir.get_name())

def get_directory_size(dir):
    total = 0
    for obj in dir.get_files():
        if type(obj) == File:
            total += obj.get_size()
        else:
            total += get_directory_size(obj)
    if total >= 4804833:
        print(dir.get_name(), total)
    return total

def at_most(dir):
    my_dirs = []
    if (answer:= get_directory_size(dir)) <= 100000:
        my_dirs.append(answer)
    for obj in dir.get_files():
        if type(obj) == Directory:
            if (answer:= get_directory_size(obj)) <= 100000:
                my_dirs.append(answer)
    return my_dirs

def main():
    base_dir = create_directories()
    get_directory_size(base_dir)



if __name__ =="__main__":
    main()
