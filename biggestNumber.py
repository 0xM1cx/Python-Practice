from bisect import bisect
import random

def getRandomNumbers():
    phoneNumbers = [9619381867]
    for i in range(1000):
        n = random.randint(9512349615, 9619181817)
        if n < phoneNumbers[0]:
            phoneNumbers.append(n)
        else:
            continue


    # biggestNumber = 0

    # for i in phoneNumbers:
    #     for b in phoneNumbers:
    #         if i > b:
    #             biggestNumber = i
    #         else:
    #             biggestNumber = b
            


    with open("phoneNumbers.txt", "w") as f:
        for i in phoneNumbers:
            f.write(str(i) + ", ")

def getBiggestNumber():
    biggest = 0
    X = [9536733525, 9537974717, 9598698103, 9587440172, 9588589811, 9566803473, 9526860065, 9616213875, 9598656338, 9617245072, 9594630389, 9578220113, 9527182580, 9524989433, 9543254293, 9586555201, 9567131492, 9531458522, 9552638581, 9549851020, 9597650482, 9540371514, 9547809198, 9551712670, 9553567600, 9577051367, 9612467225, 9591132982, 9561100988, 9614723527, 9544713381, 9559670300, 9603473366, 9582262458, 9585087865, 9573418374, 9541793060, 9570375577, 9588026158, 9591699801, 9540673612, 9530352872, 9533470204, 9609582085, 9613755580, 9568399281, 9592412901, 9540609237, 9578552470, 9617820160, 9534917278, 9535457375, 9609505907, 9574735389, 9587204962, 9548494362, 9603449589, 9544980002, 9601914545, 9539602989, 9585552154, 9519931928, 9604035398, 9615453802, 9562325039, 9614789208, 9517367957, 9539022619, 9514116126, 9580849115, 9610810531, 9615909367, 9521275631, 9608083504, 9530529082, 9561548695, 9543961244, 9519546115, 9609649217, 9590296178, 9565397463, 9601650276, 9591182327, 9602709017, 9597489008, 9512392881, 9514866533, 9605287449, 9544234812, 9612807305, 9587222653, 9615313867, 9618347044, 9569100718, 9551143433, 9516907558, 9613701545, 9541174083, 9521357201, 9605668773, 9570630412, 9526126998, 9569124421, 9608395064, 9588403335, 9526157464, 9539766651, 9612659746, 9574864013, 9527776980, 9572427100, 9582456485, 9596865329, 9607614760, 9618405526, 9542632847, 9532589397, 9570686288, 9563475495, 9558358104, 9567304241, 9583443661, 9537340137, 9608001302, 9542173527, 9614151404, 9594989337, 9605908375, 9534036212, 9557605065, 9528156248, 9532413983, 9611212314, 9591827375, 9612824067, 9523596183, 9576847164, 9533260394, 9612087709, 9592839825, 9521113637, 9515409951, 9545564684, 9529342747, 9615281339, 9541304360, 9560601208, 9526674544, 9608276429, 9529989706, 9583320005, 9581082673, 9556410874, 9533432534, 9541013718, 9540972514, 9589123886, 9589582509, 9596595735, 9587706709, 9546372046, 9572658265, 9539988457, 9522742382, 9543937970, 9527732349, 9611454174, 9570518210, 9559328942, 9613110029, 9609947812, 9600732977, 9595475273, 9591390171, 9553175412, 9602984368, 9542715453, 9551245923, 9517280507, 9560728269, 9587715335, 9614172202, 9567722502, 9579888983, 9599804884, 9601141255, 9561443915, 9571329218, 9591716508, 9591333166, 9578509693, 9606863715, 9515367877, 9522634132, 9579460657, 9534940077, 9554890629, 9544430792, 9596372667, 9578988224, 9519738747, 9573785513, 9615217505, 9578398101, 9601626370, 9597532583, 9603380065, 9544097275, 9590494566, 9614003922, 9595777293, 9528902253, 9575023180, 9534470729, 9530614308, 9519871371, 9586243135, 9557862522, 9566552900, 9597730821, 9534956976, 9609315331, 9585922466, 9570863924, 9533223942, 9610895811, 9588131116, 9546924432, 9577340940, 9516085005, 9605479929, 9583564909, 9584279721, 9529912037, 9562480548, 9574665701, 9515416591, 9536374990, 9539434588, 9605424421, 9527243920, 9582529756, 9612370703, 9518114113, 9590616877, 9531123549, 9535287316, 9544414919, 9612454094, 9578001175, 9538202550, 9558563766, 9602993226, 9592109527, 9589102548, 9531330007, 9599514758, 9559461030, 9570572406, 9593529141, 9582415935, 9533881595, 9619087939, 9614084935, 9605660260, 9537975297, 9535047245, 9557322816, 9581846263, 9606009373, 9607535502, 9561614162, 9595009021, 9599802934, 9569564102, 9580342064, 9614089297, 9534935172, 9523492158, 9530063323, 9566718428, 9556788672, 9591064705, 9530552278, 9603111772, 9608960226, 9517100317, 9587475946, 9520600056, 9607815383, 9520856061, 9532984015, 9540048957, 9597797813, 9520073070, 9526322717, 9613362213, 9591512171, 9573240033, 9612721935, 9611343408, 9519865956, 9528515084, 9615711273, 9520362138, 9535338673, 9534962157, 9547373355, 9546912907, 9573041402, 9589380578, 9608418521, 9578519371, 9565857825, 9519785298, 9580776127, 9532023142, 9565335916, 9594458070, 9524006994, 9533504140, 9520514899, 9527689369, 9525287661, 9555310037, 9518968028, 9613803011, 9518521430, 9601705486, 9556756695, 9551283509, 9514454282, 9516111580, 9524551765, 9514972111, 9603467973, 9561440525, 9584084711, 9554908730, 9606950687, 9512600308, 9567722194, 9592416821, 9560507392, 9515865775, 9559746518, 9545164440, 9542930549, 9575252090, 9574560912, 9582892632, 9523452635, 9568736414, 9562780435, 9525298039, 9577186138, 9610447337, 9581909595, 9537664202, 9567572048, 9553004614, 9518763780, 9603929050, 9581844430, 9557783115, 9567310482, 9614150713, 9524916595, 9606598311, 9607305433, 9608127475, 9545655949, 9530849649, 9553396629, 9569851027, 9543550639, 9556745246, 9554355422, 9568665118, 9516029948, 9553364924, 9598583343, 9593195104, 9555049118, 9546219746, 9558150815, 9536278424, 9575720795, 9554470804, 9522138725, 9541005455, 9560739786, 9576677621, 9544584673, 9562564182, 9546424202, 9579818108, 9517538498, 9600071297, 9600852856, 9513623529, 9521963069, 9609616924, 9592258687, 9581022243, 9557049195, 9547830700, 9529241196, 9585447254, 9521909896, 9612753431, 9618377466, 9542019498, 9593707804, 9573734616, 9610615681, 9586256680, 9514625483, 9532514650, 9524037361, 9584452130, 9604191731, 9587120172, 9581435539, 9565815441, 9522128003, 9545810576, 9533735995, 9586537477, 9562369300, 9572973005, 9561658979, 9571395546, 9600915853, 9517706687, 9599181442, 9542749171, 9613611897, 9568456083, 9538401562, 9596376017, 9521285227, 9585305170, 9581620554, 9524112970, 9581823646, 9556216352, 9534417513, 9534098279, 9568862862, 9618375412, 9575946694, 9590765443, 9573529138, 9580230950, 9559501510, 9616033577, 9612390524, 9567545353, 9525917808, 9584545041, 9592490328, 9548608407, 9612854174, 9530807609, 9588312944, 9538495217, 9547186623, 9568610300, 9607944251, 9616255173, 9524828859, 9546194714, 9540119495, 9521249790, 9528434928, 9543139560, 9567509074, 9531473826, 9580750821, 9590402698, 9578934421, 9570028624, 9517037499, 9546766143, 9536425833, 9519413290, 9605719329, 9613963214, 9549042295, 9616515899, 9537293988, 9568548878, 9592044976, 9528607864, 9586660756, 9591345112, 9542651484, 9604834197, 9616516925, 9552137528, 9540967660, 9619381867, 9543055649, 9556702108, 9541936262, 9553342141, 9512531174, 9539248104, 9532839199, 9515453445, 9525599380, 9578613563, 9572077315, 9528389340, 9580471273, 9612087913, 9609975047, 9525333834, 9521123051, 9613096150, 9596018988, 9553276460, 9609419655, 9555715827, 9558842829, 9603622622, 9607318930, 9606874245, 9522312893, 9584113464, 9524140693, 9591014169, 9558383807, 9543211577, 9564452362, 9567942741, 9569742148, 9539325443, 9561773341, 9545822875, 9512698624, 9519635877, 9555624746, 9554153685, 9521104546, 9576410062, 9551467356, 9530557998, 9538585205, 9550343411, 9553538520, 9617533625, 9529721069, 9531896508, 9588386070, 9547081710, 9547168965, 9515195622, 9584779753, 9540365700, 9596675341, 9562272068, 9536686753, 9566416535, 9532664722, 9587996732, 9562827481, 9616670775, 9614733549, 9522694871, 9609721924, 9529619999, 9572455986, 9592010611, 9544374058, 9551032482, 9533515007, 9534231964, 9600709643, 9595645614, 9581541414, 9616454250, 9571858960, 9570853184, 9544547356, 9523514038, 9514598878, 9530890471, 9584194062, 9595442597, 9591219619, 9612082709, 9562696570, 9517078382, 9561249956, 9541639019, 9561195375, 9587073894, 9577650171, 9533638611, 9570057324, 9564517812, 9531807651, 9615169373, 9610567712, 9545355401, 9512358910, 9538348489, 9542940960, 9541537104, 9606353446, 9613290847, 9569442744, 9518800067, 9601614964, 9513213762, 9538031444, 9544620982, 9552599800, 9605865881, 9548925655, 9564781711, 9596208530, 9556834597, 9565407296, 9533725581, 9562423179, 9557849771, 9531689559, 9533679640, 9530416173, 9562403784, 9519346140, 9538986696, 9608622100, 9515679471, 9528604202, 9563108673, 9599343171, 9542457624, 9583735289, 9613011378, 9551515948, 9519389697, 9575504325, 9522670904, 9524093109, 9530664770, 9597652804, 9516107211, 9603114585, 9513020737, 9613560783, 9522309034, 9546458189, 9599214343, 9584776797, 9588196464, 9565698993, 9609192911, 9533957515, 9608907638, 9616884832, 9520108760, 9547060328, 9523549849, 9567673636, 9536775960, 9537837790, 9581738236, 9564090885, 9581971909, 9539340992, 9518274079, 9609599441, 9515277918, 9518525588, 9537513214, 9551572778, 9615075330, 9567606106, 9594003591, 9561829290, 9526341490, 9543012986, 9610551414, 9546351149, 9521948761, 9618913149, 9530523761, 9528928089, 9614414023, 9577640226, 9527085342, 9546934136, 9526551105, 9540672303, 9604831209, 9544108929, 9596850003, 9578940656, 9531326239, 9526991071, 9588510583, 9545776298, 9540585842, 9521871190, 9521681205, 9612575837, 9619074715, 9569529042, 9543885558, 9554834133, 9611846041, 9537449355, 9573464274, 9525976436, 9574153839, 9616794545, 9577646340, 9565446750, 9601210221, 9611065983, 9532681836, 9512460279, 9570891119, 9557590988, 9571262045, 9514803752, 9617953446, 9561778285, 9566699174, 9595617967, 9564754233, 9606655129, 9572645998, 9568177421, 9531786556, 9614934523, 9614375848, 9548821492, 9587406486, 9554335118, 9547022223, 9619007683, 9554872825, 9561742777, 9558777383, 9571645194, 9597457177, 9540273774, 9567404859, 9530184315, 9576531693, 9537202827, 9522927902, 9601627033, 9559350538, 9592366287, 9537980428, 9596581180, 9578990856, 9531670745, 9600869637, 9555697439, 9561549739, 9548654928, 9564477910, 9577328890, 9610794370, 9525493653, 9605326217, 9556180257, 9597356163, 9527182176, 9537758289, 9568049187, 9544143888, 9595548746, 9530368536, 9564993159, 9606638126, 9519203471, 9534904459, 9611458736, 9532134978, 9575538012, 9516091439, 9584179003, 9600059602, 9526915799, 9565136326, 9571052682, 9558545580, 9538096251, 9614527407, 9525811251, 9566053257, 9522756879, 9549535170, 9618768794, 9541738710, 9566274887, 9579395905, 9532405727, 9559599801, 9566480289, 9552962390, 9573281693, 9531764437, 9591795714, 9528810659, 9614316351, 9516051426, 9556591555, 9548081685, 9599814890, 9603174508, 9615955319, 9513600395, 9609635405, 9586909411, 9566119192, 9569492690, 9584378100, 9615923935, 9516908934, 9561769954, 9570137114, 9516782096, 9587515473, 9535316160, 9546859508, 9515075943, 9606285428, 9578871083, 9541414585, 9552412444, 9512503509, 9603561974, 9519160537, 9617659156, 9547926133, 9561766677, 9574595043, 9549671007, 9544438241, 9578901907, 9551694231, 9601872334, 9592998508, 9534026730, 9566410917, 9614180077, 9517493393, 9513654833, 9578364970, 9535691234, 9519916425, 9572934345, 9598820011, 9574477276, 9571258803, 9526695557, 9569505422, 9529375461, 9552150326, 9549932311, 9613224796, 9592797411, 9586097887, 9588567268, 9520336193, 9582910314, 9589283386, 9537837750, 9552927286, 9591474103, 9584744287, 9513539865, 9590898748, 9613844172, 9580840313, 9538606542, 9533055753, 9606893011, 9601806239, 9615510938, 9597851318, 9573489488, 9618543675, 9549991643, 9527630712, 9608627105, 9567986531, 9548467898, 9570626636, 9572959968, 9586372453, 9546206604, 9582427981, 9542398761, 9527388846, 9555607452, 9614134974, 9555586141, 9539667742, 9579001862, 9599388352, 9544014644, 9534458727, 9550403556, 9571919085, 9577315394, 9538530049, 9605448453, 9539688168, 9580918757, 9559513490, 9587681837, 9515239540, 9535322156, 9615321407, 9565966293, 9557635792, 9568986792, 9576094837, 9544290975, 9577402132, 9545965475, 9547666900, 9591699917, 9574480217, 9596571720, 9574503898, 9585507425, 9607211160, 9547088226, 9556118457, 9559029552, 9549824290, 9514477437, 9548127389, 9571810367, 9562428032, 9541551905, 9535814859, 9562241109, 9580520464, 9514487241, 9516316584, 9585623165, 9574132487, 9572897022, 9562801640, 9557548964, 9613920503, 9519451021, 9613296318, 9553072905, 9579521025, 9524981997, 9568803812, 9611615142, 9550324213, 9535678862, 9522664205, 9528470626, 9618291282, 9561724302, 9522844308, 9545840271, 9520783482, 9598239631, 9522092071, 9520101305, 9550914657, 9557867976, 9517261169, 9594077172, 9564727160, 9525821353, 9584898889, 9521161937, 9518703657, 9568748893, 9611247160, 9544983247, 9548174591, 9573294969, 9559595712, 9542075510, 9522073371, 9588671071, 9608502895, 9586879023, 9601840544, 9559686825, 9550657381, 9560868343] 
    print(max(X))



getBiggestNumber()