data_file = '450131651746463754 802951855452979200 795419482297729064 835513437601136690 439841325110525992 870909391099035698 511145660796633088 834203522119106580 880082063145988096 826024961852309576 795604321357660160 413016291272687616 762828736504266763 849751388824010822 830926690578202684 833420797318004746 616826208612778014 844553957686116383 843895864673828924 419635692629393429 768000354016428032 459379324567420938 837460200465367060 839803535285289010 841807651423387649 745287326455955526 543944276556513302 808505902800961597 904055476562591774 716263014990479401 560163884229591041 734438540464881798 935175251376099358 730609887263981588 908097592464912424 656985423566077994 833106351119007775 919776340125839391 595281442779693068 439592238499102724 895519599213297695 773460845862715404 793345585381376001 567599507387187222 708382896184098816 917853257387364372 733830864777248798 498631900139618306 920358451236991016 442727818745610243 335635813188501505 901445720341622794 707394024243200121 803002298812334081 698204631108550706 934887944983031868 530045223703937044 797583486277779476 932808197885001738 670838386185207869 859077363899695105 899172412921348096 596359174791757842 849741895382466600 541620748784238602 642969054277271565 473718411235688450 621113575590592523 842964887217897483 535278076918104076 316299268216324096 852661477168775168 818241584524951603 864646754175156254 812237973391015966 924756516400136222 326410294895312907 581981575072317460 529035823530639386 409845497185173507 779466979668918313 705950046708957185 453369846567141376 592721086408425472 444654674315051008 424744217454182404 802235428992319529 343408761714769920 843581319426342922 539480993544011798 855141080344428594 769720104308310056 863202893904609280 849447773053124638 582375749600673794 869376572572962818'
with open(r"nonwithStanding.txt", 'w') as sexy:
    data = data_file.split()
    for x in data:
        sexy.write("\n" + x)