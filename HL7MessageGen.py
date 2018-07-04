###############################################################################
# HL7 MESSAGE GENERATOR
# Ken Sturgis v1 |  05DEC17
###############################################################################
from tkinter import *
import os
import random
import datetime
import string

###############################################################################
# FUNCTIONS
###############################################################################

# Randomly pick and assign first and last name
def setName():
    listFirst = ['Bob', 'John', 'Adam', 'William', 'Jason', 'Ken', 'Kishan', 'Jessica', 'Olivia',
                'Emma', 'Amber', 'Mia', 'Emily', 'Sarah', 'David', 'Isaac', 'Leah', 'Steve',
                'Mohammad', 'Madison', 'Victoria', 'David', 'Henry', 'Ian', 'Nick', 'Jennifer',
                'Hector', 'Aaron', 'Mike', 'Steve', 'Juan', 'Leeroy', 'Ashley', 'Heather']
    listLast = ['Smith', 'Johnson', 'Williams', 'Davis', 'Brown', 'Jones', 'Miller',
                'Wilson', 'Jackson', 'Thompson', 'Robinson', 'Lewis', 'Lopez', 'Carter',
                'Henderson', 'Peterson', 'Howard', 'Wood', 'Ramirez', 'Russell', 'Cox',
                'Diaz', 'Hill', 'Moore', 'Martinez', 'Green', 'Reed', 'Patel', 'Humphrey']
    firstName = random.choice(listFirst)
    lastName = random.choice(listLast)

    return firstName, lastName

# Set the start and end dates
# YYYYMMDDHHMMSS
def setDate():
    currentDate = datetime.datetime.now()
    ndate = str(currentDate)
    junk = ['-', ':', ' ']
    ndate = ndate.translate({ord(x): '' for x in junk})

    # Remove the seconds
    sec = '.'
    ndate = ndate.split(sec, 1)[0]

    # Add 5 mins to start date
    ndate = int(ndate) + 500
    edate = ndate
    ndate = str(ndate)

    # Add 7 days to end date
    edate = int(edate) + 7000000
    edate = str(edate)
    return ndate, edate

# Set MRN to random 8 digits
def setMRN():
    mrn = string.digits
    mrn = (''.join(random.sample(mrn * 8, 8)))
    return mrn

# Set LabelID to random 10 Alphanumeric chars
def setLabelID():
    labelID = string.ascii_uppercase + string.digits
    labelID = (''.join(random.sample(labelID * 10, 10)))
    return labelID

# Set random SIG Freq
def setSIG():
    freqSIG = [
        'once^T1',
        'daily^D5',
        'daily^T2',
        'q12h^T1',
        'q6h^T1',
        'q2h^T1',
        'q1h^T1',
        'q12h M/W/F^T1',
        'every other night^T1',
        '2 times a week^'
    ]

    sig = random.choice(freqSIG)

    return sig

# Random pick a Drug Block
def setDrug():
    chemoDrugList = ([
        # 1 - BLINAtumomab
        'RXE||NOADM1^PHARMACY GENERATED ORDER(PHARMACY GENERATED ORDER)|1||DOSE|injection|IVCI once at 5 ml/hr for 48 hours. 9 mcg daily x 2 days = 18mcg over 48 hr thr 0.2 micron filter||||||||M034DWCVGX|||||||48.00|5|ml/hr' + "\n" +
        'RXR|IVCI^IVCI' + "\n" +
        'NTE|1|P|BLINAtumomab inj: add 3 mL SWFI to 35 mcg vial|Administrative^Instruction (non-printing)' + "\n" +
        'NTE|2|P|IVCI once at 5 ml/hr for 48 hours. 9 mcg daily x 2 days = 18 mcg over 48 hr through 0.2 micron filter.  Prepared:  12:00 noon on 11 /1/17.|Admin Instructions^Admin Instructions' + "\n" +
        'RXC|A|NOADM1^PHARMACY GENERATED ORDER(PHARMACY GENERATED ORDER)^^B|1|DOSE' + "\n" +
        'RXC|A|74740549^BLINAtumomab [multi-day] injection 35 mcg (12.5 mcg/mL)(BLINAtumomab [multi-day] injection 35 mcg (12.5 mcg/mL))^^A|18|mcg'  + "\n" +
        'RXC|A|74739939^IV solution stabilizer for BLINATUMOmab inj 1 mL(IV solution stabilizer for BLINATUMOmab inj 1 mL)^^A|4.8|ml'  + "\n" +
        'RXC|B|74719253^normal saline 1 mL for qs or custom volume(normal saline for qs or custom volume)^^A|233.76|ml',
        # 2 - Fluorouracil
        'RXE||74711136^fluorouracil injection 50 mg/mL, 100 mL(fluorouracil injection 50 mg/mL, 100 mL)|7000||mg|injection|||||||||M034DWCXJS|||||||168.00|1.3|ml/hr' + "\n" +
        'RXR|IVCI^IVCI' + "\n" +
        'NTE|1|P|500 mg/ m2/ day x 2.01 m2 = 1000 mg/day x 7 Days = 7000 mg total dose infuse at 1.3 ml/hr|Special Instructions^Special Instructions (do NOT use for label comments)' + "\n" +
        'RXC|A|74711136^fluorouracil injection 50 mg/mL, 100 mL(fluorouracil injection 50 mg/mL, 100 mL)^^B|7000|mg' + "\n" +
        'RXC|A|74739244^Dosi-Fuser Pump(Dosi-Fuser Pump)^^A|1|each' + "\n" +
        'RXC|B|74719253^normal saline 1 mL for qs or custom volume(normal saline for qs or custom volume)^^A|78|ml',
        #3 - Mesna
        'RXE||74716960^mesna injection 100 mg/mL, 10 mL(MESNEX injection 100 mg/mL)|90||mg|injection|To begin 1/2 hour pre Cyclophosphamide infusion||||||||M034DWCRWL|||||||24.00|44.12|ml/hr' + "\n" +
        'RXR|IVCI^IVCI' + "\n" +
        'NTE|1|P|To begin 1/2 hour pre Cyclophosphamide infusion|Admin Instructions^Admin Instructions' + "\n" +
        'NTE|2|P|Rate = mL/hr|Special Instructions^Special Instructions (do NOT use for label comments)' + "\n" +
        'RXC|A|74716960^mesna injection 100 mg/mL, 10 mL(MESNEX injection 100 mg/mL)^^B|90|mg' + "\n" +
        'RXC|B|74733437^normal saline 1,000 mL + 58 mL overfill(normal saline 1000 mL + 58 mL overfill)^^A|1058|ml',
        #4 - DOXOrubicin
        'RXE||74708678^DOXOrubicin injection 2 mg/mL, 100 mL(ADRIAMYCIN injection 2 mg/mL, 100 mL)|19||mg|injection|can be co-administered via Y-site||||||||M034DWCSHM|||||||24.00|22.56|ml/hr' + "\n" +
        'RXR|IVCI^IVCI' + "\n" +
        'NTE|1|P|can be co-administered via Y-site|Admin Instructions^Admin Instructions' + "\n" +
        'NTE|2|P|Rate = mL/hr|Special Instructions^Special Instructions (do NOT use for label comments)' + "\n" +
        'RXC|A|74708678^DOXOrubicin injection 2 mg/mL, 100 mL(ADRIAMYCIN injection 2 mg/mL, 100 mL)^^B|19|mg' + "\n" +
        'RXC|B|74707738^dextrose 5% in water 500 mL + 32 mL overfill(dextrose 5% in water 500 mL + 32 mL overfill)^^A|532|ml'
        ])

    drug = random.choice(chemoDrugList)

    return drug

# Generate an HL7 message with the results of the functions above
def HL7Message(nFirst, nLast, nFacility, nDate, eDate, nMRN, nLabelID, nDrug, orderFlag, sig):
    message = 'MSH|^~\&|PCS|SCM|HLTCVO||' + nDate + '||RDE^O01|9012978600401100|D|2.3' + "\n" + 'PID|||' + nMRN + '||' + nLast + '^' + nFirst + '||20101027' + "\n" + 'PV1||Inpatient|NS-9^920^A^' + nFacility + '||||||||||||||||8455646178^^^IPACCT' + "\n" + 'ORC|'+ orderFlag +'|' + nLabelID + '^PCS|' + nLabelID + '||||^' + sig + '^' + nDate + '^' + eDate +'^Inpatient Chemo|||||MDRAY^Attending^Doc' + "\n" + nDrug + "\n"

    return message

def setStatusBar(statusmessage):
    status_ent.set(statusmessage)
    return

###############################################################################
# MAIN
###############################################################################
def mainapp():

    textfile = open('HL7messages.txt', 'w')

    count = count_ent.get()
    facility = facility_ent.get()

    i = 0
    while(i < count):
        # Get a Name, Date, MRN, LabelID and Drug(s)
        firstName, lastName = setName()
        startDate, endDate = setDate()
        mrn = setMRN()
        labelID = setLabelID()
        drugList = setDrug()
        sig = setSIG()
        orderFlag = 'NW'  # For now all orders are NEW, this variable for future development with CA orders

        # Compile the entire HL7 message
        message = HL7Message(firstName, lastName, facility, startDate, endDate, mrn, labelID, drugList, orderFlag, sig)
        print(message, file=textfile)

        status_ent.set('Waiting for input...')

        i = i + 1

    textfile.close()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    hl7file = dir_path + '\HL7message.txt'
    status = "Text file created at: " + hl7file
    setStatusBar(status)

###############################################################################
# TKINTER
###############################################################################
root = Tk()
root.title("HL7 Message Generator")
root.geometry("400x180+100+100")
root.resizable(0,0)
heading = Label(root, text="HL7 MESSAGE GENERATOR", font=("arial", 15, "bold"), fg="steelblue").pack()
subheading = Label(root, text="Internal Use Only | v1", font=("arial", 7), fg="steelblue").place(relx=0.99, rely=0.15, anchor=NE)

# Vars
global count_ent
global facility_ent
global status_ent
count_ent = IntVar()
facility_ent = StringVar()
status_ent = StringVar()

# Fields
Label(root, text="Number of Orders: ", font=("arial", 10, "bold")).place(x=40, y=50)
Entry(root, textvariable=count_ent, width=5).place(x=180, y=50)
Label(root, text="Facility Name: ", font=("arial", 10, "bold")).place(x=40, y=75)
Entry(root, textvariable=facility_ent).place(x=180, y=75)

# Buttons
but_generate = Button(root, width=15, text="Generate File", command=mainapp).place(relx=0.5, rely=0.75, anchor=CENTER)

# Note
# Label(root, text="", font=("arial", 7), fg="steelblue").place(relx=0.99, rely=0.91, anchor=SE)

# Status Bar
status = Label(root, textvariable=status_ent, bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
setStatusBar('Waiting for Input...')

# KEEP WINDOW OPEN
root.mainloop()
