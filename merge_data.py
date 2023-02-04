import csv

# getting data from files
order_info = open("20220419-1967-2021-OrderOfCanada.csv", encoding='mac_roman')
order_bios = open("04012023-bio.xlsx - Sheet1.csv")

info = [x for x in csv.reader(order_info)]
bios = [x for x in csv.reader(order_bios)]

order_info.close()
order_bios.close()

# just some index and field checks
c = 0
for i in info[0]:
    print(c, i, bios[0].index(i) if i in bios[0] else -1)
    c += 1

c = 0
for i in bios[0]:
    print(c, i, info[0].index(i) if i in info[0] else -1)
    c += 1

# rewrite the rows with award info as well
new_csv_file = open("merged_order_of_canada_data.csv", "w")
csv_writer = csv.writer(new_csv_file)

for i in range(8014):
    csv_writer.writerow([info[i][0], info[i][1], info[i][2], info[i][3], info[i][4], info[i][5], info[i][6], info[i][7], info[i][8], info[i][9], info[i][10], info[i][11], info[i][12], info[i][13], info[i][14], info[i][15], info[i][16], info[i][17], info[i][18], info[i][19], info[i][20], info[i][21], info[i][22], info[i][23], info[i][24], info[i][25], info[i][26], info[i][27], info[i][28], info[i][29], bios[i][7], bios[i][8], bios[i][9], bios[i][10], bios[i][11], bios[i][12], bios[i][13], bios[i][14], bios[i][15], bios[i][16], bios[i][17], bios[i][18], bios[i][19], bios[i][20], bios[i][21], bios[i][22], bios[i][23]])

new_csv_file.close()

