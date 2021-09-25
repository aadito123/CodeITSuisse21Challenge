import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

class Solve:
    def __init__(self, interview):
        self.questions = interview['questions']
        self.max = interview['maxRating']        

    def solve(self):
        for question in self.questions:
            maxiFrom = max(question, key=lambda interval: interval['from'])
            logging.info("maxiFrom: {}".format(maxiFrom))
            miniFrom = min(question, key=lambda interval: interval['to'])
            logging.info("miniFrom: {}".format(miniFrom))
        return {}

@app.route('/stig/perry', methods=['POST'])
def evaluateOptopt():
    interviews = request.get_json()
    #logging.info("data sent for evaluation {}".format(data))
    result = []
    for interview in interviews:
        result.append(Solve(interview).solve())
    logging.info("My result :{}".format(result))
    return json.dumps(result)

'''
[{'questions': [[{'from': 522655228, 'to': 636942065}], [{'from': 199165753, 'to': 437740464}], [{'from': 664497500, 'to': 772862433}], [{'from': 346906678, 'to': 759385309}], [{'from': 665083147, 'to': 944232888}], [{'from': 693620699, 'to': 701955495}], [{'from': 64667477, 'to': 748992355}], [{'from': 332254364, 'to': 709444217}], [{'from': 29346043, 'to': 145716414}], [{'from': 12025544, 'to': 39930260}], [{'from': 169798089, 'to': 710915689}], [{'from': 121268546, 'to': 271888059}], [{'from': 116561958, 'to': 585089256}], [{'from': 57727558, 'to': 275346568}], [{'from': 245318164, 'to': 375131440}], [{'from': 222832430, 'to': 763536443}], [{'from': 540411076, 'to': 891044333}], [{'from': 522934564, 'to': 672152743}], [{'from': 116705088, 'to': 165665650}], [{'from': 607945554, 'to': 935064533}], [{'from': 603492539, 'to': 661786836}], [{'from': 273114375, 'to': 958439633}], [{'from': 95526248, 'to': 870385711}], [{'from': 261657489, 'to': 450009546}], [{'from': 710888398, 'to': 755834994}], [{'from': 150100451, 'to': 364331993}], [{'from': 587869478, 'to': 749903263}], [{'from': 137536119, 'to': 911911982}], [{'from': 271139509, 'to': 931562699}], [{'from': 698728594, 'to': 885098961}], [{'from': 282178719, 'to': 517484847}], [{'from': 125005455, 'to': 844859574}], [{'from': 616062647, 'to': 895948566}], [{'from': 693547301, 'to': 932117990}], [{'from': 291668220, 'to': 360287571}], [{'from': 410292384, 'to': 963662538}], [{'from': 492488125, 'to': 493948643}], [{'from': 646382578, 'to': 972079901}], [{'from': 78063647, 'to': 272766422}], [{'from': 24037404, 'to': 848213944}], [{'from': 435395997, 'to': 493559480}], [{'from': 252879182, 'to': 584133343}], [{'from': 150150150, 'to': 595083574}], [{'from': 939537558, 'to': 941583649}], [{'from': 251544673, 'to': 258735454}], [{'from': 252523362, 'to': 670114214}], [{'from': 328366211, 'to': 687772122}], [{'from': 11188299, 'to': 306407773}], [{'from': 645425284, 'to': 987111007}], [{'from': 29372727, 'to': 882544010}], [{'from': 721164727, 'to': 842107202}], [{'from': 49138268, 'to': 707185723}], [{'from': 584135595, 'to': 787919783}], [{'from': 305631281, 'to': 324022073}], [{'from': 377754495, 'to': 476292934}], [{'from': 181726826, 'to': 648610456}], [{'from': 522140861, 'to': 652706538}], [{'from': 381181231, 'to': 761487372}], [{'from': 372975388, 'to': 385756123}], [{'from': 116241332, 'to': 422045611}], [{'from': 674987507, 'to': 951791514}], [{'from': 16330418, 'to': 377455335}], [{'from': 45514412, 'to': 495930708}], [{'from': 270784127, 'to': 299185392}], [{'from': 336861057, 'to': 937268959}], [{'from': 563707103, 'to': 950279139}], [{'from': 375284667, 'to': 449478241}], [{'from': 178750608, 'to': 549016197}], [{'from': 654496175, 'to': 881081129}], [{'from': 163052131, 'to': 689530808}], [{'from': 478719631, 'to': 568997227}], [{'from': 329278865, 'to': 596984591}], [{'from': 29107939, 'to': 368641946}], [{'from': 10712697, 'to': 183202786}], [{'from': 55332905, 'to': 520909725}], [{'from': 124545002, 'to': 644472632}], [{'from': 115238651, 'to': 706495131}], [{'from': 172325846, 'to': 201127764}], [{'from': 435521423, 'to': 480438968}], [{'from': 251252932, 'to': 762389397}], [{'from': 158619290, 'to': 902463848}], [{'from': 32728173, 'to': 630401845}], [{'from': 70616514, 'to': 946300478}], [{'from': 48768890, 'to': 866858898}], [{'from': 447846402, 'to': 906424136}], [{'from': 49844362, 'to': 968838988}], [{'from': 529195942, 'to': 898601686}], [{'from': 72498990, 'to': 783243803}], [{'from': 106133601, 'to': 618574371}], [{'from': 144667355, 'to': 930740023}], [{'from': 395788632, 'to': 654059243}], [{'from': 807123287, 'to': 845506728}], [{'from': 805921830, 'to': 826957297}], [{'from': 779589841, 'to': 910229026}], [{'from': 168099250, 'to': 508509060}], [{'from': 300544632, 'to': 924277970}], [{'from': 50458486, 'to': 917275460}], [{'from': 75486067, 'to': 411899056}], [{'from': 728920206, 'to': 777320076}], [{'from': 645025333, 'to': 775453276}], [{'from': 839184359, 'to': 909664274}], [{'from': 786420, 'to': 962926395}], [{'from': 182082762, 'to': 696440423}], [{'from': 208862130, 'to': 854570172}], [{'from': 253034788, 'to': 653450820}], [{'from': 529196528, 'to': 813142545}], [{'from': 329436824, 'to': 508894138}], [{'from': 12406960, 'to': 31391404}], [{'from': 453884174, 'to': 986561876}], [{'from': 4114467, 'to': 27890709}], [{'from': 686214663, 'to': 694015073}], [{'from': 532357720, 'to': 729156653}], [{'from': 602183489, 'to': 655675197}], [{'from': 113334830, 'to': 756035254}], [{'from': 685807936, 'to': 718157297}], [{'from': 733015850, 'to': 782854255}], [{'from': 63710822, 'to': 648585168}], [{'from': 197652080, 'to': 397876445}], [{'from': 473999643, 'to': 888534265}], [{'from': 151707585, 'to': 681137006}], [{'from': 7475343, 'to': 458475648}], [{'from': 361425987, 'to': 401185832}], [{'from': 253137530, 'to': 776394896}], [{'from': 203469086, 'to': 808243115}], [{'from': 233097216, 'to': 267764510}], [{'from': 706832509, 'to': 853873454}], [{'from': 102865697, 'to': 540930587}], [{'from': 555070462, 'to': 782696331}], [{'from': 824623764, 'to': 948453211}], [{'from': 79361456, 'to': 776132136}], [{'from': 162012389, 'to': 656024993}], [{'from': 645852570, 'to': 741092489}], [{'from': 695896363, 'to': 825531798}], [{'from': 13767287, 'to': 472144236}], [{'from': 589401004, 'to': 953384085}], [{'from': 244108606, 'to': 446403885}], [{'from': 437918551, 'to': 600647603}], [{'from': 415628914, 'to': 579151539}], [{'from': 435474030, 'to': 836058382}], [{'from': 509280032, 'to': 930569144}], [{'from': 3170519, 'to': 170286605}], [{'from': 141764850, 'to': 695816785}], [{'from': 30152631, 'to': 486279751}], [{'from': 90114949, 'to': 575740111}], [{'from': 312880780, 'to': 448146005}], [{'from': 35103476, 'to': 437999493}], [{'from': 363091977, 'to': 978644747}], [{'from': 821581056, 'to': 936646952}], [{'from': 285018218, 'to': 819152802}], [{'from': 659883164, 'to': 714733088}], [{'from': 277893940, 'to': 729660146}], [{'from': 212931063, 'to': 789811026}], [{'from': 48550918, 'to': 415536408}], [{'from': 174414242, 'to': 506745056}], [{'from': 374332279, 'to': 751746537}], [{'from': 232157492, 'to': 806136746}], [{'from': 856911347, 'to': 867499658}], [{'from': 279833966, 'to': 818059508}], [{'from': 581669338, 'to': 874845942}], [{'from': 283866120, 'to': 685232130}], [{'from': 238015935, 'to': 762058755}], [{'from': 748377910, 'to': 868722276}], [{'from': 105011213, 'to': 614135540}], [{'from': 815709068, 'to': 978938519}], [{'from': 263273115, 'to': 617936007}], [{'from': 437163176, 'to': 719514636}], [{'from': 619916042, 'to': 794803451}], [{'from': 40403543, 'to': 782049057}], [{'from': 245315225, 'to': 782984307}], [{'from': 53370120, 'to': 769997062}], [{'from': 162672808, 'to': 787180421}], [{'from': 121137801, 'to': 184858555}], [{'from': 16420170, 'to': 341164306}], [{'from': 298879664, 'to': 608543772}], [{'from': 385267655, 'to': 418068492}], [{'from': 68994240, 'to': 606152326}], [{'from': 276164645, 'to': 591781504}], [{'from': 181625359, 'to': 702368987}], [{'from': 559169780, 'to': 739399443}], [{'from': 582923589, 'to': 726396587}], [{'from': 501346595, 'to': 894377483}], [{'from': 154759964, 'to': 455915206}], [{'from': 226071132, 'to': 933824924}], [{'from': 543404180, 'to': 904210359}], [{'from': 230813146, 'to': 577269503}], [{'from': 225515579, 'to': 679215354}], [{'from': 389952773, 'to': 545628758}], [{'from': 133669620, 'to': 923470683}], [{'from': 441537547, 'to': 550161146}], [{'from': 811496691, 'to': 961716018}], [{'from': 235796536, 'to': 773699385}], [{'from': 511827488, 'to': 782010992}], [{'from': 15798338, 'to': 31503027}], [{'from': 260002034, 'to': 603492539}], [{'from': 449436384, 'to': 966637496}], [{'from': 15672334, 'to': 949126572}], [{'from': 675093283, 'to': 747957613}], [{'from': 132247129, 'to': 396888457}], [{'from': 386571218, 'to': 688710774}], [{'from': 368125170, 'to': 600268370}], [{'from': 128865217, 'to': 986952549}], [{'from': 20921343, 'to': 275372292}], [{'from': 696287070, 'to': 704687299}], [{'from': 44173480, 'to': 240887283}], [{'from': 598812156, 'to': 901070840}], [{'from': 103241506, 'to': 781327269}], [{'from': 8935734, 'to': 291186520}], [{'from': 328362938, 'to': 835915793}], [{'from': 179472729, 'to': 739531295}], [{'from': 300064305, 'to': 739573878}], [{'from': 937399713, 'to': 984735890}], [{'from': 453833181, 'to': 619595877}], [{'from': 530682350, 'to': 800216788}], [{'from': 278564822, 'to': 523630567}], [{'from': 339672358, 'to': 725047805}], [{'from': 22699469, 'to': 41551484}], [{'from': 222663375, 'to': 290323389}], [{'from': 4920837, 'to': 414678968}], [{'from': 87688082, 'to': 654221648}], [{'from': 31485280, 'to': 437386611}], [{'from': 709035005, 'to': 975961319}], [{'from': 248854442, 'to': 615086316}], [{'from': 783512999, 'to': 984059371}], [{'from': 266556370, 'to': 655696329}], [{'from': 634877011, 'to': 700941815}], [{'from': 732351667, 'to': 959529942}], [{'from': 79263381, 'to': 922808530}], [{'from': 769445317, 'to': 935820793}], [{'from': 305562909, 'to': 328837203}], [{'from': 292130197, 'to': 493410597}], [{'from': 108942928, 'to': 266782283}], [{'from': 114572315, 'to': 459697187}], [{'from': 300363600, 'to': 497600255}], [{'from': 641960417, 'to': 990093401}], [{'from': 303665546, 'to': 608241451}], [{'from': 189996939, 'to': 923262718}], [{'from': 59186983, 'to': 660253600}], [{'from': 186630056, 'to': 742493026}], [{'from': 361498361, 'to': 664921595}], [{'from': 190388044, 'to': 787830838}], [{'from': 243468740, 'to': 853495106}], [{'from': 258478800, 'to': 691215458}], [{'from': 128370402, 'to': 453338034}], [{'from': 234262653, 'to': 819634019}], [{'from': 25726167, 'to': 399192723}], [{'from': 814517764, 'to': 950188116}], [{'from': 96378821, 'to': 779344336}], [{'from': 237932215, 'to': 277585549}]]]'''