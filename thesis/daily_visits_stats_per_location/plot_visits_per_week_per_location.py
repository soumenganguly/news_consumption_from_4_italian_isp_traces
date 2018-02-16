import sys
import matplotlib.pyplot as plt

input_file_1 = open(sys.argv[1],'rb')
input_file_2 = open(sys.argv[2],'rb')
input_file_3 = open(sys.argv[3],'rb')
input_file_4 = open(sys.argv[4],'rb')

file_read_1 = input_file_1.read()
file_read_2 = input_file_2.read()
file_read_3 = input_file_3.read()
file_read_4 = input_file_4.read()

s1 = file_read_1.replace('\t','  ')
s2 = file_read_2.replace('\t','  ')
s3 = file_read_3.replace('\t','  ')
s4 = file_read_4.replace('\t','  ')

data_1 = s1.split('\n')
data_2 = s2.split('\n')
data_3 = s3.split('\n')
data_4 = s4.split('\n')


def calculate_views(data):
    week = {}
    k=0
    #for i in range(20):                        # Uncomment for analysis for half year
    for i in range(52):                         # Uncomment for analysis for a whole year
        views = []
        #print "Week %d"%(i+1)
        #print data[k:k+7]
        for j in data[k:k+7]:
            views.append(j.split('  ')[2])
            sum = 0
            for value in views:
                sum = sum + int(value)
        week[(i+1)] = sum
        k=k+7
    return week


if __name__ == '__main__':
    x1 = range(1,53)                          # for whole year
    #x1 = range(1,21)                         # half a year
    y1 = []

    x2 = range(1,53)
    #x2 = range(1,21)
    y2 = []
    
    x3 = range(1,53)
    #x3 = range(1,21)
    y3 = []

    x4 = range(1,53)
    #x4 = range(1,21)
    y4 = []

    loc_1 = calculate_views(data_1)
    for i in loc_1:
        y1.append(int(loc_1[i]))

    loc_2 = calculate_views(data_2)
    for i in loc_2:
        y2.append(int(loc_2[i]))

    loc_3 = calculate_views(data_3)
    for i in loc_3:
        y3.append(int(loc_3[i]))

    loc_4 = calculate_views(data_4)
    for i in loc_4:
        y4.append(int(loc_4[i]))


    plt.plot(x1,y1, label='City-1: Residential', ls=':') #PDF
    plt.plot(x2,y2, label='City-1: Campus', ls='--') #POLI
    plt.plot(x3,y3, label='City-2: Residential', ls='-.') #PUL
    plt.plot(x4,y4, label='City-1: Work') #UMB

    plt.legend()

    plt.grid()

    plt.xticks(range(1,53,4))
    plt.xlabel('Week')
    plt.ylabel('# of views')

    plt.title('Visits from year 2015 (Without scrapy)')
    plt.show()


    input_file_1.close()
    input_file_2.close()
    input_file_3.close()
    input_file_4.close()
