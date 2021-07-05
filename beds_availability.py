# input

'''
#print (userInput)
#"book aniket 987654321 20 mysecurebed C 3"
#"discharge mysecurebed C 3"
#"Freebeds C"
#"OK"
'''
userInput = ""
userInputArr = []
bed_dict = {}
total_beds_dict = {}

def print_bed_status (hospital):
    bed_str = ""
    for bed_num in range (1, 101):
        bed_key = hospital + str(bed_num)
        if bed_key not in bed_dict:
            bed_str = bed_str + str(bed_num) + ' '
    return bed_str

class Patient:
    name = ""
    age = 0
    phoneNumber = -1
    password = ""

    def __init__(self, name, age, phoneNumber, password):
        self.age = age
        self.name = name
        self.password = password
        self.phoneNumber = phoneNumber
    
    def __str__(self):
        return "[ " + self.name + " | " + self.age + " | " + self.phoneNumber + " | " + self.password

if __name__ == '__main__':
        
    while (True):
        userInput = input()
        userInputArr = userInput.split(' ')
    
        print (userInputArr)
    
        if (userInputArr[0] not in ['book', 'discharge', 'Freebeds', 'OK', 'Totalbeds']):
            print ("""Available options are: "book", "discharge", "Freebeds", "OK" and "Totalbeds". Please try again.""")
            continue

        if userInputArr[0] == "OK":
            print ("thanks for using beingartifex corona management system")
            exit(0)
        elif userInputArr[0] == "book" and len(userInputArr) == 7 and userInputArr[5] >= 'A' and userInputArr[5] <= 'J' and int(userInputArr[6]) >= 1  and int(userInputArr[6]) <= int(100):
            bed_dict_key = str(userInputArr[5]) + str(userInputArr[6])

            if bed_dict_key in bed_dict:
                print ("bed is already booked. please try another bed.")
            else:
                bed_dict_val = Patient(userInputArr[1], userInputArr[3], userInputArr[2], userInputArr[4])
                bed_dict[bed_dict_key] = bed_dict_val
                print ("bed reserved. please try a new command.")
                #book aniket 987654321 20 mysecurebed C 3
        elif userInputArr[0] == "discharge" and len(userInputArr) == 4 and userInputArr[2] >= 'A' and userInputArr[2] <= 'J' and int(userInputArr[3]) >= 1  and int(userInputArr[3]) <= 100:
            #discharge mysecurebed C 3
            bed_dict_key = str(userInputArr[2]) + str(userInputArr[3])
            if bed_dict_key in bed_dict and bed_dict[bed_dict_key].password == userInputArr[1]:
                print ("patient discharged.")
                del bed_dict[bed_dict_key]
            else:
                print ("patient details not found. please try again.")
        elif userInputArr[0] == "Freebeds" and len(userInputArr) == 2:
            bed_status_str = print_bed_status(userInputArr[1])
            print (bed_status_str)
        elif userInputArr[0] == "Totalbeds" and len(userInputArr) == 1:
            for key, value in bed_dict.items():
                if key[0] in total_beds_dict:
                   total_beds_dict[key[0]] += 1 
                else :
                    total_beds_dict[key[0]] = 1
            print ("Total Beds: " + str(total_beds_dict))
