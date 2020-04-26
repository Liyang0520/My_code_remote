with open('1output.csv', 'r', newline='') as filereader:
    with open('1_read.csv', 'w', newline='') as filewriter:
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list, '\n')
        filewriter.write(','.join(map(str,header_list)) + '\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write((','.join(map(str, row_list)))+'\n')
filewriter.close()
filereader.close()