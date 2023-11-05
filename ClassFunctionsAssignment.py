class FunctionAssignment():
    def Subfields():
        print("Sub-fields in AI are:")
        A=["Machine Learning","Neural Network","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for AI in A:
            print(AI)
            New=("AI")
            
    def oddEven():
        Num1=int(input("Enter a number :"))
        if((Num1%2)==0):
            print(Num1,"is Even number")
            msg="The Entered number is EVEN"
        else:
            print(Num1,"is odd number")
            msg="The Entered number id ODD"
            
    def Eligible():
        A=input("Your Gender :")
        B=int(input("Your Age :"))
        if((A=="Male" and B>=21) or (A=="Female" and B>=18)):
            print("Eligible")
            msg:"Eligible"
        else:
            print("Not Eligible")
            msg="Not Eligible"
            
    def Percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Add=(sub1+sub2+sub3+sub4+sub5)
        percent=(Add/5)
        print("Total :",Add)
        msg="Add"
        print("Percentage :",percent)
        msg="percent"
        
    def Triangle():
        L1=int(input("Height :"))
        L2=int(input("Breadth :"))
        A=L1*L2
        Area=A/2
        print("Area Formula : (Height*Breadth)/2")
        print("Area of the Triangle :",Area)
        msg="Area"
        T1=int(input("Height1 :"))
        T2=int(input("Height2 :"))
        T3=int(input("Breadth :"))
        Peri=T1+T2+T3
        print("Perimeter Formula : Height1+Height2+Breadth")
        print("Perimeter of Triangle :",Peri)
        msg="Peri"