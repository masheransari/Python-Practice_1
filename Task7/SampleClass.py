class SampleClass:
    datamember = [4, 3, 5, 6, 5, 1, 10, 8, 2, 7, 9, 6, 2]

    def __init__(self):
        output = []

        for x in SampleClass.datamember:
            if x not in output:
                output.append(x)
        print(output)

    def showArray():
        print("Our Array is: ")
        for (i, item) in enumerate(SampleClass.datamember, start=1):
            print(i, item)
        print("-----------------------------------------")

    def smallest():
        small = []
        for i in SampleClass.datamember:
            if i < 6:
                small.append(i)
        print(small)
        print("-----------------------------------------")

    def sortArray():
        print("Sorted Data:")
        sortedList = SampleClass.datamember
        min = 0

        for i in range(0, len(sortedList)):
            for j in range(0, len(sortedList)):
                if (sortedList[i] < sortedList[j]):
                    min = sortedList[i]
                    sortedList[i] = sortedList[j]
                    sortedList[j] = min
        for (i, item) in enumerate(sortedList, start=1):
            print(i, item)
        print("-----------------------------------------")
