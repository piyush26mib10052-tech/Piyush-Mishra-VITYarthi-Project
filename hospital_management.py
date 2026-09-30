import time

# ============================================
#     VITYARTHI HOSPITAL MANAGEMENT SYSTEM
# ============================================

patients_list=[]
appointments_list=[]
bills=[]

def get_int(prompt):
    while True:
        value=input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid whole number.")

# --------------------------
#   1.PATIENT REGISTRATION
# --------------------------

def addpatient():
    print("\n---- Add New Patient ---")
    patient_id=input("Enter Id:")

    for i in range(len(patients_list)):
        if patients_list[i]["ID"]==patient_id:
            print("This patient already exists!")
            return

    name=input("Enter Name:")
    age=get_int("Enter Age:")
    gender=input("Gender:")
    phone=input("Phone:")
    address=input("Address:")
    bloodgroup=input("Blood Group:")
    disease=input("Disease:")

    temp_patient={
        "ID":patient_id,
        "NAME":name,
        "AGE":age,
        "GENDER":gender,
        "PHONE":phone,
        "ADDRESS":address,
        "BLOOD GROUP":bloodgroup,
        "DISEASE":disease,
        "STATUS":"ADMITTED"
    }

    patients_list.append(temp_patient)
    print("Patient Saved!!!\n")

# --------------------------
#   2.VIEW PATIENT DETAILS
# --------------------------

def show_all():
    print("\nSHOWING ALL PATIENTS:")
    if len(patients_list)==0:
        print("Patient Not Found.")
    else:
        for p in patients_list:
            print("ID:",p["ID"],"| NAME:",p["NAME"],"| AGE:",p["AGE"],"| DISEASE:",p["DISEASE"])
            print()

# ------------------------
#     3.SEARCH PATIENT
# ------------------------

def search():
    search_id=input("\nEnter id to search:")
    for p in patients_list:
        if p["ID"]==search_id:
            print("Patient Found!")
            print("NAME:",p["NAME"])
            print("AGE:",p["AGE"])
            print("BLOOD GROUP:",p["BLOOD GROUP"])
            print("STATUS:",p["STATUS"])
            return
    print("Sorry,No Patient Found With This ID")

# --------------------------
#      4.UPDATE PATIENT
# --------------------------

def update_patient():
    patient_id=input("\nWhose details you want to change? Enter ID:")
    for i in range(len(patients_list)):
        if patients_list[i]["ID"]==patient_id:
            print("Enter new details now:")
            patients_list[i]["NAME"]=input("New Name:")
            patients_list[i]["AGE"]=get_int("New Age:")
            patients_list[i]["DISEASE"]=input("New Disease:")
            print("Details Updated.")
            return
    print("Not Found.")

# ---------------------------
#    5.BOOKING APPOINTMENT
# ---------------------------

def book_appt():
    patient_id=input("\nPatient ID for appointment:")
    for p in patients_list:
        if p["ID"]==patient_id:
            doc=input("Doctor Name:")
            date=input("Date:")
            appt_time=input("Time:")
            appointments_list.append([patient_id,p["NAME"],doc,date,appt_time])
            print("Appointment Booked!")
            return
    print("REGISTER PATIENT FIRST!")

# -------------------------
#         6.BILLING
# -------------------------

def make_bill():
    patient_id=input("\nEnter patient id to bill:")
    for p in patients_list:
        if p["ID"]==patient_id:
            print("Enter amounts:")
            doc_fee=get_int("Doctor Fee:")
            meds=get_int("Medicine cost:")
            room=get_int("Room Rent:")
            total=doc_fee+meds+room
            bills.append({"ID":patient_id,"NAME":p["NAME"],"TOTAL":total})
            print("-------------------")
            print("Total Bill for",p["NAME"],": Rs.",total)
            print("-------------------")
            return
    print("Patient id wrong")

# -------------------------
#        7.DISCHARGE
# -------------------------

def discharge():
    patient_id=input("\nEnter id to discharge:")
    for p in patients_list:
        if p["ID"]==patient_id:
            p["STATUS"]="DISCHARGED"
            print(p["NAME"],"is discharged now.Going Home!")
            return
    print("Could not find patient")

# -------------------------
#        8.MAIN MENU
# -------------------------

while True:
    print("\n============================================")
    print("    VITYARTHI HOSPITAL MANAGEMENT SYSTEM    ")
    print("============================================")
    print("1.PATIENT REGISTRATION")
    print("2.VIEW PATIENT DETAILS")
    print("3.SEARCH PATIENT")
    print("4.UPDATE PATIENT")
    print("5.BOOKING APPOINTMENT")
    print("6.BILLING")
    print("7.DISCHARGE")
    print("8.EXIT")

    opt=input("Type your choice:")

    if opt=="1":
        addpatient()
    elif opt=="2":
        show_all()
    elif opt=="3":
        search()
    elif opt=="4":
        update_patient()
    elif opt=="5":
        book_appt()
    elif opt=="6":
        make_bill()
    elif opt=="7":
        discharge()
    elif opt=="8":
        print("Exiting...")
        time.sleep(1)
        print("Bye!")
        break
    else:
        print("Wrong option,try again.")
