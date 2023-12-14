from pathlib import Path
class Solution:
    def getCalibrationValues(self):
        calibrationValues = []
        filePath = Path(__file__).with_name('day1.txt')
        with filePath.open('r') as file:
            for value in file.readlines():
                firstVal, lastVal = '', ''
                calibrationValue = 0
                for index in value:
                    if index.isdigit() and firstVal == '':
                        firstVal = index
                        lastVal = index
                        calibrationValue = int(firstVal + lastVal)
                    elif index.isdigit() and firstVal != '':
                        lastVal = index
                        calibrationValue = int(firstVal + lastVal)
                calibrationValues.append(calibrationValue)
        return calibrationValues

    def sumCalibrationValues(self):
        sum = 0
        calibrationVals = self.getCalibrationValues()
        print(calibrationVals[0])
        for val in calibrationVals:
            sum += val
        return sum

x = Solution()
finalSum = x.sumCalibrationValues()
print('finalSum: ', finalSum)