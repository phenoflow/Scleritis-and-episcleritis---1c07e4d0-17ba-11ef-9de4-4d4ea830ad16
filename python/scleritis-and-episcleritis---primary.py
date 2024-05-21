# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"F4K0.11","system":"readv2"},{"code":"F4K0200","system":"readv2"},{"code":"F4K0000","system":"readv2"},{"code":"FyuD800","system":"readv2"},{"code":"F4K0600","system":"readv2"},{"code":"F4K0.00","system":"readv2"},{"code":"F4K0z00","system":"readv2"},{"code":"F4K0500","system":"readv2"},{"code":"F4K0.12","system":"readv2"},{"code":"F4K0300","system":"readv2"},{"code":"F4K0711","system":"readv2"},{"code":"F4K0100","system":"readv2"},{"code":"F4K0700","system":"readv2"},{"code":"F4K0400","system":"readv2"},{"code":"51523.0","system":"readv2"},{"code":"40365.0","system":"readv2"},{"code":"47820.0","system":"readv2"},{"code":"6783.0","system":"readv2"},{"code":"15996.0","system":"readv2"},{"code":"28123.0","system":"readv2"},{"code":"44859.0","system":"readv2"},{"code":"5318.0","system":"readv2"},{"code":"136.0","system":"readv2"},{"code":"65835.0","system":"readv2"},{"code":"35599.0","system":"readv2"},{"code":"37665.0","system":"readv2"},{"code":"101293.0","system":"readv2"},{"code":"40647.0","system":"readv2"},{"code":"H15.0","system":"readv2"},{"code":"H15.1","system":"readv2"},{"code":"H19.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('scleritis-and-episcleritis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["scleritis-and-episcleritis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["scleritis-and-episcleritis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["scleritis-and-episcleritis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
