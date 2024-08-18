###HOW TO USE.  https://www.motorangutan.com/sku-table
###https://www.motorangutan.com/sku-table/0000+1111+2222
from multiprocessing import Process
import csv

def multipro():

    ifile = open('products_export.csv', "r")  ##Need to export only when new products have been added since the last time.
    reader = csv.reader(ifile)

    outfile = open('PriceUpdateFiles/Website-newPrices.csv', "w")
    writer = csv.writer(outfile)
    ##writer.writerow(('PRODUCT_ID','SKU','name','Cost','List_price','Sell_price'))
    writer.writerow(('Handle','Title','Option1 Name','Option1 Value','Option2 Name','Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Inventory Qty','Variant Price','Variant Compare At Price','Cost per item'))


    ############Sullivans###################################################


    print ('Starting Sullivans ------------------------------------------------------------')

    notfound = open('PriceUpdateFiles/Sullivans-notfound.csv', "w")
    notfoundfile = csv.writer(notfound)

    outfileb = open('PriceUpdateFiles/Sullivans-logfile.csv', "w")
    logfile = csv.writer(outfileb)
    ##logfile.writerow(('PRODUCT_ID','SKU','name','New Cost','List_price','New Sell_price','Old Cost','Old List Price','Old Sell Price','Sell Factor'))
    logfile.writerow(('Handle','Title','Option1 Name','Option1 Value','Option2 Name','Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Inventory Qty','Variant Price','Variant Compare At Price','Cost per item','OLD Variant Price','OLD Variant Compare At Price','OLD Cost per item','NOTES/Sell Factor'))
    sultextfile = open('Data/Sullivans_Web_Price_List_New.txt', 'r')
    sulreader = csv.reader((line.replace('\0','') for line in sultextfile), delimiter="\t")
    sulfile = list(sulreader)

    for row in reader:
    #     line = []

         for sulrow in sulfile:
              if sulrow[0] == 'PART NO':
                   continue
              if sulrow == sulfile[-1]:
                   notfoundfile.writerow(row)
                   ## IF product disappears I need to set qty to zero.  
                   ##writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], 0, row[19], row[20],row[46]))
                   ##logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], 0, row[19], row[20] ,row[46], '', '', row[46], 'NOT FOUND'))

    ##          sulrow = line.split("\t")
              sulsku = sulrow[0]
              try:
    #               print sulrow[0]
                   float(sulrow[11])
              except ValueError:
                   print((row[1], ' not found'))
                   notfoundfile.writerow(row)
                   break
              if row[20] in (None, ""):  ### IF compare at price is blank.  
                   row[20] = 0

              if (row[13] == sulsku): 
                   origListPrice = float(row[20])
                   origSellPrice = float(row[19])
    #               print origListPrice
                   print ('they are equal')
                   sulPrice = float(sulrow[11])    
    #               print sulPrice
                   qty = int(sulrow[19])
                   if (qty < 3):
                        qty = 0

                   if 'O' in sulrow[22]:  ## CHecking for closeouts
                        sellPrice = round(float(sulrow[9]) / 0.78 + 14, 2)    
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, sulPrice,sulrow[10]))
                        ##writer.writerow((row[0], row[1], row[2], sulrow[10], sulPrice, sellPrice))
                        ##logfile.writerow((row[0], row[1], row[2], sulrow[10], sulPrice, sellPrice, row[3], row[4], row[5], round(float(row[5]) / origListPrice, 2)))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, sulPrice ,sulrow[10], origSellPrice, '', row[46], 'CLOSEOUT'))

                   elif (origListPrice == 0):  #Selling at MSRP
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sulPrice, '',sulrow[10]))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sulPrice, '',sulrow[10], origSellPrice, '', row[46]))
                        print ('price is 0 and sell price changed')
                        break
                   elif (origListPrice != 0):  #Selling at a discount on MSRP.
                        sellPrice = round(round(float(row[19]) / origListPrice, 2) * sulPrice, 2)
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, sulPrice,sulrow[10]))
                        ##writer.writerow((row[0], row[1], row[2], sulrow[10], sulPrice, sellPrice))
                        ##logfile.writerow((row[0], row[1], row[2], sulrow[10], sulPrice, sellPrice, row[3], row[4], row[5], round(float(row[5]) / origListPrice, 2)))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, sulPrice ,sulrow[10], origSellPrice, '', row[46], round(float(row[19]) / origListPrice, 2)))
                        print ('price is NOT 0 and sell price changed')
                        break
                   else:
                        print ('last else statement' )
                        break
    notfound.close()
    outfileb.close()
    sultextfile.close()
    ##########Helmet House###################################################################
    ifile = open('PriceUpdateFiles/Sullivans-notfound.csv', "r")
    reader = csv.reader(ifile)

    print('Starting Helmet House ------------------------------------------------------------')

    notfound = open('PriceUpdateFiles/HelmetHouse-notfound.csv', "w")
    notfoundfile = csv.writer(notfound)

    outfileb = open('PriceUpdateFiles/HelmetHous-logfile.csv', "w")
    logfile = csv.writer(outfileb)
    logfile.writerow(('Handle','Title','Option1 Name','Option1 Value','Option2 Name','Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Inventory Qty','Variant Price','Variant Compare At Price','Cost per item','OLD Variant Price','OLD Variant Compare At Price','OLD Cost per item','NOTES/Sell Factor'))
    hhfile = open('Data/master.csv', 'r')
    hhreader = csv.reader((line.replace('\0','') for line in hhfile), delimiter=",")
    next(hhreader)
    hhtextfile = list(hhreader)
    for row in reader:
         for hhrow in hhtextfile:

              if hhrow == hhtextfile[-1]:
                   notfoundfile.writerow(row)
                   ##writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], 0, row[19], row[20],row[46]))
                   ##logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], 0, row[19], row[20],row[46], '', '', row[46], 'NOT FOUND'))

                   break
    #          print hhrow
    #          if len(hhrow) < 1:
    #               print 'End of Helmet House'
    #               break
              hhsku = hhrow[0]
    ##          if (len(hhsku) > 10):           ##################Need to convert WEBSTIE TO HAVE - in SKUS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ##               hhsku = hhsku.replace("-","")
    #          print row[1], hhsku
              if row[20] in (None, ""):  ### IF compare at price is blank.  
                   row[20] = 0
              if (row[13] == hhsku): 
                   origListPrice = float(row[20])
                   origSellPrice = float(row[19])
    #               print origListPrice
                   print('they are equal')
                   hhPrice = float(hhrow[4])
                   if (hhrow[5] == '12+'):
                        hhrow[5] = 12
                   if (hhrow[6] == '12+'):
                        hhrow[6] = 12
                   west = int(float(hhrow[5]))
                   east = int(float(hhrow[6]))
                   qty = int(west + east) 

                   if (qty < 3):
                        qty = 0

                   if hhrow[8] == 'N':
                        hhCloseoutPrice = round(float(hhrow[3]) / 0.8 + 10, 2)
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, hhCloseoutPrice, hhPrice,hhrow[3]))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, hhCloseoutPrice, hhPrice ,hhrow[3], origSellPrice, '', row[46], 'CLOSEOUT'))

                        ##writer.writerow((row[0], row[1], row[2], hhrow[3], hhPrice, hhCloseoutPrice))
                        ##logfile.writerow((row[0], row[1], row[2], hhrow[3], hhPrice, hhCloseoutPrice, row[3], row[5]))
                        print('price is 0 and sell price changed')
                        break
                   elif (origListPrice == 0):
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, hhPrice, '',hhrow[3]))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, hhPrice, '',hhrow[3], origSellPrice, '', row[46]))

    ##                    writer.writerow((row[0], row[1], row[2], hhrow[3], row[4], hhPrice))
    ##                    logfile.writerow((row[0], row[1], row[2], hhrow[3], row[4], hhPrice, row[3], row[5]))
                        print('price is 0 and sell price changed')
                        break
                   elif (origListPrice != 0):
                        sellPrice = round(round(float(row[19]) / origListPrice, 2) * hhPrice, 2)
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, hhPrice  ,hhrow[3]))
                        ##writer.writerow((row[0], row[1], row[2], hhrow[3], hhPrice, sellPrice))
                        ##logfile.writerow((row[0], row[1], row[2], hhrow[3], hhPrice, sellPrice, row[3], row[4], row[5], round(float(row[5]) / origListPrice, 2)))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, hhPrice ,hhrow[3], origSellPrice, '', row[46], round(float(row[19]) / origListPrice, 2)))
                        print('price is NOT 0 and sell price changed')
                        break
                   else:
                        print('last else statement') 
                        break
    notfound.close()
    outfileb.close()
    hhfile.close()

    ##########Tucker Rocky###################################################################
    ifile = open('PriceUpdateFiles/HelmetHouse-notfound.csv', "r")
    reader = csv.reader(ifile)
    print('Starting Tucker Rocky  ------------------------------------------------------------')

    itrQtyfile = open('Data/invupd', "r")
    trQtyfile = list(csv.reader(itrQtyfile))

    notfound = open('PriceUpdateFiles/TuckerRocky-notfound.csv', "w")
    notfoundfile = csv.writer(notfound)

    outfileb = open('PriceUpdateFiles/TuckerRocky-logfile.csv', "w")
    logfile = csv.writer(outfileb)
    logfile.writerow(('Handle','Title','Option1 Name','Option1 Value','Option2 Name','Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Inventory Qty','Variant Price','Variant Compare At Price','Cost per item','OLD Variant Price','OLD Variant Compare At Price','OLD Cost per item','NOTES/Sell Factor'))
    trfile = list(open('Data/itemmstrnew', "r", encoding='ISO-8859-1'))
    #reader.next()
    for row in reader:
         for line in trfile:
              if line == trfile[-1]:
                   notfoundfile.writerow(row)
                   ##writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], 0, row[19], row[20], row[46]))
                   ##logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], 0, row[19], row[20] ,row[46], '', row[46], 'NOT FOUND'))
                   break
              try:
                   float(line[56:64])
              except ValueError:
                   print(row[1], ' not found')
                   break



              if row[20] in (None, ""):  ### IF compare at price is blank.  
                   row[20] = 0

              ##print(row[13].replace('\'',''), '--------',line[0:6])
              if (row[13].replace('\'','') == line[0:6]): 
                   origListPrice = float(row[20])
                   origSellPrice = float(row[19])
    #               print origListPrice
                   print('they are equal')
                   trPrice = float(line[56:64])

                   qty = 0
                   for line2 in trQtyfile:
                        ##print(line2)
                        ##print((row[13].replace('\'',''), '--------',line2[0]))
                        if (line2[0] == row[13].replace('\'','')):
                             qty = int(line2[1]) 
                             if (qty < 3):
                                  qty = 0
                             break

                   if line[36:37] == 'C':
                        trCloseoutPrice = round(float(line[38:46]) / 0.8 + 10, 2)
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, trCloseoutPrice, trPrice,line[38:46]))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, trCloseoutPrice, trPrice ,line[38:46], origSellPrice, '', row[46], 'CLOSEOUT'))
                        ##writer.writerow((row[0], row[1], row[2], line[46:54], trPrice, trCloseoutPrice))
                        ##logfile.writerow((row[0], row[1], row[2], line[46:54], trPrice, trCloseoutPrice, row[3], row[5], 'CLOSEOUT'))
                        print('price is 0 and sell price changed')
                        break
                   elif (origListPrice == 0):
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, trPrice, '',line[38:46]))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, trPrice, '', line[38:46], origSellPrice, '', row[46]))
                        ##writer.writerow((row[0], row[1], row[2], line[46:54], row[4], trPrice))
                        ##logfile.writerow((row[0], row[1], row[2], line[46:54], row[4], trPrice, row[3], row[5]))
                        print('price is 0 and sell price changed')
                        break
                   elif (origListPrice != 0):
                        sellPrice = round(round(float(row[19]) / origListPrice, 2) * trPrice, 2)

                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, trPrice  ,line[38:46]))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, trPrice ,line[38:46], origSellPrice, '', row[46], round(float(row[19]) / origListPrice, 2)))
                        ##writer.writerow((row[0], row[1], row[2], line[46:54], trPrice, sellPrice))
                        ##logfile.writerow((row[0], row[1], row[2], line[46:54], trPrice, sellPrice, row[3], row[5], round(float(row[5]) / origListPrice, 2)))
                        print('price is NOT 0 and sell price changed')
                        break
                   else:
                        print('last else statement') 
                        break
    notfound.close()
    outfileb.close()

    ##########Western Powersports ###################################################################
    print('Starting Western Powersports ------------------------------------------------------------')

    ifile = open('PriceUpdateFiles/TuckerRocky-notfound.csv', "r")
    reader = csv.reader(ifile)

    notfound = open('PriceUpdateFiles/WPS-notfound.csv', "w")
    notfoundfile = csv.writer(notfound)


    outfileb = open('PriceUpdateFiles/WPS-logfile.csv', "w")
    logfile = csv.writer(outfileb)
    logfile.writerow(('Handle','Title','Option1 Name','Option1 Value','Option2 Name','Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Inventory Qty','Variant Price','Variant Compare At Price','Cost per item','OLD Variant Price','OLD Variant Compare At Price','OLD Cost per item','NOTES/Sell Factor'))
    ##logfile.writerow(('PRODUCT_ID','SKU','name','New Cost','List_price','New Sell_price','Old Cost','Old List Price','Old Sell Price','Sell Factor'))

    iwpsfile = open('Data/WPS_Daily_Combined.csv', encoding="utf8", errors='ignore')
    next(iwpsfile)
    wpslistfile = list(csv.reader(iwpsfile, delimiter=","))


    for row in reader:
    #     line = []
         for wpsrow in wpslistfile:
              if wpsrow == wpslistfile[-1]:
                   notfoundfile.writerow(row)
                   ##writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], 0, row[19], row[20],row[46]))
                   ##logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], 0, row[19], row[20] ,row[46], '', '', row[46], 'CLOSEOUT'))

              wpssku = wpsrow[0]
              try:

                   float(wpsrow[5])
              except ValueError:
                   print(row[1], ' not found')
                   notfoundfile.writerow(row)
                   break
              if (row[1] == wpssku): 
                   origListPrice = float(row[4])
                   origSellPrice = float(row[5])
    #               print origListPrice
                   print('they are equal')
                   wpsPrice = float(wpsrow[4])
    #               print sulPrice
              if row[20] in (None, ""):  ### IF compare at price is blank.  
                   row[20] = 0
              if (row[13] == wpssku): 
                   origListPrice = float(row[20])
                   origSellPrice = float(row[19])
    #               print origListPrice
                   print('they are equal')
                   wpsPrice = float(wpsrow[4])
                   wpsCost = float(wpsrow[5])
                   qty = int(float(wpsrow[24]))

                   closeout = 'false'
                   if wpsrow[10] == 'N':
                        wpsCloseoutPrice = wpsPrice * 0.82
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, wpsCloseoutPrice, wpsPrice,wpsCost))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, wpsCloseoutPrice, wpsPrice ,wpsCost, origSellPrice, '', row[46], 'CLOSEOUT'))

                        ##writer.writerow((row[0], row[1], row[2], wpsrow[5], wpsPrice, wpsCloseoutPrice))
                        ##logfile.writerow((row[0], row[1], row[2], wpsrow[5], wpsPrice, wpsCloseoutPrice, row[3], row[5],'CLOSEOUT'))
                        print('price is 0 and sell price changed')
                        break
                   elif (origListPrice == 0 and wpsPrice != origSellPrice):
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, wpsPrice, '',wpsCost))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, wpsPrice, '',wpsCost, origSellPrice, '', row[46]))

                        #writer.writerow((row[0], row[1], row[2], wpsrow[5], row[4], wpsPrice))
                        ##logfile.writerow((row[0], row[1], row[2], wpsrow[5], row[4], wpsPrice, row[3], row[5]))
                        print('price is 0 and sell price changed')
                        break
                   elif (origListPrice != 0 and wpsPrice != origListPrice):
                        sellPrice = round(round(float(row[19]) / origListPrice, 2) * wpsPrice, 2)
                        writer.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, wpsPrice  ,wpsCost))
                        logfile.writerow((row[0], row[1], row[7],row[8],row[9],row[10],row[11],row[12], row[13], qty, sellPrice, wpsPrice ,wpsCost, origSellPrice, '', row[46], round(float(row[19]) / origListPrice, 2)))
                        
                        ##writer.writerow((row[0], row[1], row[2], wpsrow[5], wpsPrice, sellPrice))
                        #logfile.writerow((row[0], row[1], row[2], wpsrow[5], wpsPrice, sellPrice, row[3], row[4], row[5], round(float(row[5]) / origListPrice, 2)))
                        print('price is NOT 0 and sell price changed')
                        break
                   else:
                        print('last else statement') 
                        break

    notfound.close()
    outfileb.close()

    ####LOOP THROUGH NOT FOUND AND SET THEM ALL TO ZERO QTY and PRINT them in the outfile inventory file.  
    #### DO THIS AT THE END OF THE SCRIPT!!!!

    outfile.close()
    ifile.close()

def main():

    p = Process(target=multipro)
    p.start()

if __name__ == '__main__':
    main()


