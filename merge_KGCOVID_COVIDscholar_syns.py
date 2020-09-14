

KGCOVID_syns_p = "uniprot_sars-cov-2.gpi"
COVIDscholar_syns_p = "synonyms_list_COVIDscholar.txt"

with open(KGCOVID_syns_p, 'r') as fk:
    count = 0
    # skip header

    line = fk.readline()
    while line.find("!") == 0:
        line = fk.readline()
        #print(line)

    countORFs = 0
    countORFs_total = 0

    print("summary\tORF\tcommon\tonlykg\tonlycs\tkg_syns\tcs_syns")

    while line:
        #print(line)
        line_split = line.split("\t")
        #print(len(line_split))
        cur_gene_name = line_split[2]
        cur_syns = line_split[4].replace("\n","").split("|")
        print(cur_syns)
        countORFs_total = countORFs_total + 1
        #print(cur_gene_name)
        found = 0
        foundkgcs = 0
        notfoundcs = 0
        notfoundkg = 0
        cssyncount = 0
        with open(COVIDscholar_syns_p, 'r') as fc:
            linec = fc.readline()
            while linec:#and found == 0:
                linec_split = linec.replace("\n","").split(", ")
                #print(linec_split)
                if cur_gene_name in linec_split:
                    cssyncount = len(linec_split)
                    #print("found")
                    found = 1
                    countORFs = countORFs + 1

                    for syn in cur_syns:
                        if syn in linec_split:
                            print("found kg/cs :"+syn+":")
                            foundkgcs = foundkgcs + 1
                        else:
                            print("not found in cs :" + syn+":")
                            notfoundcs = notfoundcs + 1

                    for synin in linec_split:
                        if synin in cur_syns:
                            pass
                            #print("found cs :" + synin+":")
                        else:
                            if synin[0] != "(":
                                print("not found in kg :" + synin+":")
                                notfoundkg = notfoundkg +1

                    break
                linec = fc.readline()
        print("summary\t"+cur_gene_name+"\t"+str(foundkgcs)+"\t"+str(notfoundcs)+"\t"+str(notfoundkg)+"\t"+str(len(cur_syns))+"\t"+str(cssyncount))
        #print("found "+str(found))
        if found == 0:
            print("did not find "+cur_gene_name)
        line = fk.readline()

    print('{:d} {:d}'.format(countORFs, countORFs_total) )#countORFs+" / "+countORFs_total)

