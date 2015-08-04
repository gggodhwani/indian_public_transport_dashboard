import csv
INPUT_FILE = "data/transport_data.csv"
OUTPUT_FILE = "data/transport_data_updated.csv"

class DataTransformer(object):
    def __init__(self):
        self.headers = None
        self.data_list = []
        self.state_id = None

    def transform_data(self):
        with open(INPUT_FILE, "rb") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                if not self.headers:
                    self.headers = row
                    self.data_list.append(row[2:])
                else:
                    if self.state_id == row[3]:
                        for index in range(len(row[4:])):
                            data_point = row[4+index] 
                            if not data_point == "NaN":
                                data_point = eval(data_point)
                                if self.data_list[-1][2+index] == "NaN":
                                    self.data_list[-1][2+index] = data_point
                                else:
                                    self.data_list[-1][2+index] += data_point
                    else:
                        new_data_row = []
                        new_data_row.append(row[2])
                        new_data_row.append(row[3])
                        for index in range(len(row[4:])):
                            data_point = row[4+index] 
                            if not data_point == "NaN":
                                data_point = eval(data_point)
                            new_data_row.append(data_point)
                        self.data_list.append(new_data_row)
                        self.state_id = row[3]
        with open(OUTPUT_FILE, "wb") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',') 
            for row in self.data_list:
                try:
                    csv_writer.writerow(row)
                except Exception, e:
                    print(e)
                    print(row)

if __name__ == '__main__':
    obj = DataTransformer()
    obj.transform_data()
