import re

ok=1
while(ok==1):
    print("Type 1 to introduce your ID and get your results.\n")
    print("Type 2 to get all of the data.\n")
    print("Type 3 to get only the results with benign tumors\n")
    print("Type 4 to get only the results with malignant tumors\n")
    print("Type 5 to get data with unknown results.\n")
    print("Type 6 to exit.\n")
    y=input("Input: ")
    if y=='1':
        while True:
            x=input('Type your ID: ')
            if not re.match('^([0-9]{5,7})$',x):
                print("Invalid ID")
            else:
                break
        pattern2=re.compile(x+r',(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?)')
        with open('data/breast-cancer-wisconsin.data','r') as f:
            contents=f.read()
            print("\nYour results: \n")
            matches2=pattern2.search(contents)
            print("ID: "+str(x))
            print("Clump Thickness: "+str(matches2.group(1)))
            print("Uniformity of Cell Size: "+str(matches2.group(2)))
            print("Uniformity of Cell Shape : "+str(matches2.group(3)))
            print("Marginal Adhesion: "+str(matches2.group(4)))
            print("Single Epithelial Cell Size: "+str(matches2.group(5)))
            print("Bare Nuclei: "+str(matches2.group(6)))
            print("Bland Chromatin: "+str(matches2.group(7)))
            print("Normal Nucleoli: "+str(matches2.group(8)))
            print("Mitoses: "+str(matches2.group(9)))
            if(matches2.group(10)==4):
                print("Class: "+str(matches2.group(10))+" (malignant)")
            else:
                print("Class: "+str(matches2.group(10))+" (benign)")
            print()
    if y=='2':
        pattern=re.compile(r'(\d{5,7}),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?)')
        count=0
        with open('data/breast-cancer-wisconsin.data','r') as f:
            contents=f.read()
            matches=pattern.finditer(contents)
            for match in matches:
                print("ID: "+str(match.group(1)))
                print("Clump Thickness: "+str(match.group(2)))
                print("Uniformity of Cell Size: "+str(match.group(3)))
                print("Uniformity of Cell Shape : "+str(match.group(4)))
                print("Marginal Adhesion: "+str(match.group(5)))
                print("Single Epithelial Cell Size: "+str(match.group(6)))
                print("Bare Nuclei: "+str(match.group(7)))
                print("Bland Chromatin: "+str(match.group(8)))
                print("Normal Nucleoli: "+str(match.group(9)))
                print("Mitoses: "+str(match.group(10)))
                print("Class: "+str(match.group(11)))
                count+=1
                print()
            print(count)
    if y=='3':
        pattern3=re.compile(r'(\d{5,7}),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),'+'2')
        count=0
        with open('data/breast-cancer-wisconsin.data','r') as f:
            contents=f.read()
            matches=pattern3.finditer(contents)
            z=input("Do you want to see all of the data or just the IDs of the patients? Type 1 for all of the data and 2 for just the IDs: ")
            if z=='1':
                for match in matches:
                    print("ID: "+str(match.group(1)))
                    print("Clump Thickness: "+str(match.group(2)))
                    print("Uniformity of Cell Size: "+str(match.group(3)))
                    print("Uniformity of Cell Shape : "+str(match.group(4)))
                    print("Marginal Adhesion: "+str(match.group(5)))
                    print("Single Epithelial Cell Size: "+str(match.group(6)))
                    print("Bare Nuclei: "+str(match.group(7)))
                    print("Bland Chromatin: "+str(match.group(8)))
                    print("Normal Nucleoli: "+str(match.group(9)))
                    print("Mitoses: "+str(match.group(10)))
                    print("Class: 2 (benign)")
                    count+=1
                    print()
            elif z=='2':
                for match in matches:
                    print("ID: "+str(match.group(1)))
                    print()
            print(count)
    if y=='4':
        pattern3=re.compile(r'(\d{5,7}),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),'+'4')
        count=0
        with open('data/breast-cancer-wisconsin.data','r') as f:
            contents=f.read()
            matches=pattern3.finditer(contents)
            for match in matches:
                print("ID: "+str(match.group(1)))
                print("Clump Thickness: "+str(match.group(2)))
                print("Uniformity of Cell Size: "+str(match.group(3)))
                print("Uniformity of Cell Shape : "+str(match.group(4)))
                print("Marginal Adhesion: "+str(match.group(5)))
                print("Single Epithelial Cell Size: "+str(match.group(6)))
                print("Bare Nuclei: "+str(match.group(7)))
                print("Bland Chromatin: "+str(match.group(8)))
                print("Normal Nucleoli: "+str(match.group(9)))
                print("Mitoses: "+str(match.group(10)))
                print("Class: 4 (malignant)")
                count+=1
                print()
            print(count)
    if y=='5':
        pattern=re.compile(r'(\d{5,7}),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?),(\d+|\?)')
        count=0
        with open('data/breast-cancer-wisconsin.data','r') as f:
            contents=f.read()
            matches=pattern.finditer(contents)
            for match in matches:
                if(match.group(2)=='?' or match.group(3)=='?' or match.group(4)=='?' or match.group(5)=='?' or match.group(6)=='?' or match.group(7)=='?' or match.group(8)=='?' or match.group(9)=='?' or match.group(10)=='?' or match.group(11)=='?'):
                    print("ID: "+str(match.group(1)))
                    print("Clump Thickness: "+str(match.group(2)))
                    print("Uniformity of Cell Size: "+str(match.group(3)))
                    print("Uniformity of Cell Shape : "+str(match.group(4)))
                    print("Marginal Adhesion: "+str(match.group(5)))
                    print("Single Epithelial Cell Size: "+str(match.group(6)))
                    print("Bare Nuclei: "+str(match.group(7)))
                    print("Bland Chromatin: "+str(match.group(8)))
                    print("Normal Nucleoli: "+str(match.group(9)))
                    print("Mitoses: "+str(match.group(10)))
                    print("Class: "+str(match.group(11)))
                    count+=1
                    print()
            print(count)
    if y=='6':
        ok=0
