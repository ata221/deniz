import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random
import requests
import shutil
from bs4 import BeautifulSoup
import time
from time import ctime
from time import sleep
import os
import feedparser
import pyfiglet
import art
from art import *

os.system("cls")

client = discord.Client()
bot_prefix = "!"
bot = commands.Bot(command_prefix = bot_prefix)

mucizeler = [
"Deniz, hacıya 25 defa gittiği halde ona hacı ünvanı verilmemiştir",
"Deniz askere giderken babasına 'Artık bu evin en büyüğü sensin' demiştir",
"Deniz soğan keserken soğanın gözleri yaşarır",
"Grahambell telefonu icat ettiğinde Deniz'den 3 cevapsız araması vardı",
"Deniz karada yüzebilir",
"Bir gün Deniz ve Superman ölümüne kavga etti. Kaybeden donunu pantolonunun üstüne giyecekti",
"Bir kez Deniz'e tabancayla ateş edildi. Zorlu geçen bir haftanın sonunda mermi hayatını kaybetti",
"Bir gün Deniz ile Flash yarıştılar. Kaybeden ise hayatının kalanında kırmızı tayt giyecekti",
"Tabut taşıyan zencilerin cenazesinde zencilerin tabutunu Deniz taşıdı",
"Bir gün Deniz ile arkadaşları tüplü dalış yapar. Herkes çıktıktan 1.5 saat sonra Deniz çıkar ve 'Tüpümü almayı unutmuşum' der",
"Deniz doğduğunda imamın kulağına ezan okumuştur",
"Deniz oyunda araba sürerken tuşlara daha sert basarsa araba daha hızlı gider",
"Denizin küçükken kumları ile taşları bir araya getirmesi sonucu Everest Dağı ortaya çıkmıştır",
"Deniz Instagram'da bir fotoğrafı paylaşmadan önce o fotoğraf 1500000 like almıştır",
"Deniz yaşlanmaz, sadece şekil değiştirir",
"Deniz kendi korumalarını korur",
"Deniz saat takmaz, saatin kaç olduğuna karar verir",
"Deniz, olmayan bir filmi izleyebilir",
"Deniz için imkansız diye bir şey yok. İmkansız için Deniz diye bir şey var",
"Deniz, 1 kuşla 5 taş vurabilir",
"Denizin osurmasına deprem deniliyor",
"Deniz aynı anda hem hapşurup hem de hapşurmayabilir",
"Deniz, zıplamadan havada takla atabilir",
"Deniz insanın bir sonraki evrimleşmiş türüdür",
"Deniz gay değildir seks yaptığı erkek kız olur",
"Deniz karşıdan karşıya geçerken arabalar sağına soluna bakar",
"Deniz uzun yıllar sigara içmiştir. Sonunda sigara kansere yakalanmıştır",
"Deniz yarasa çorbası içmiştir ve yarasa korona olmuştur",
"Deniz korku filmi izlerken film Deniz'den korkmuştur",
"Denizin çocuk yapması için kadına ihtiyacı yoktur",
"Deniz, öğretmenine ev ödevi veriyor",
"Deniz döner kapıyı açabilir",
"Denizin çıktığı bir mahkemede hakim, suçlu bulunmuştur",
"Saklıköy aslında Deniz'den saklanıyor",
"Deniz Ankara'da gemi kazası yapmıştır",
"Yürüyen merdiven Deniz'i gördüğünde koşmaya başlar",
"Dünyada oksijen biterse sadece Deniz hayatta kalabilir",
"Mark Zuckerberg Facebook'u ilk bulduğunda Deniz'den arkadaşlık isteği vardı",
"Deniz dolu silahla rus ruleti oynamış ve kazanmıştır",
"Bir gün Deniz nefes almayı unutmuş, oksijenler boğularak ölmüş",
"Denizin horlamasına gök gürültüsü deniliyor",
"Ozon tabakası, güneşi Denizden korumak içindir",
"Deniz doğduğu hastanenin inşaatında çalıştı",
"Deniz suya girdiğinde ıslanmaz",
"Deniz içki içtikten sonra bardak sarhoş olmuştur",
"Deniz'in beyni yoktur. Çünkü hiçbir beyin o vücudu idare edemez",
"Ateistler Deniz'i görünce iman eder çünkü hiçbir tesadüf böyle bir insan yaratamaz",
"Deniz kurallara uymaz, kurallar Deniz'e uyar",
"Cinler Deniz'e musallat olmaz, Deniz cinlere musallat olur",
"Deniz paraşütle atlarken paraşütü açılmadı. Ertesi gün paraşütü iade etti",
"Deniz hiçbir zaman hastalanmaz çünkü mikroplar ona bulaşacak kadar aptal değildir",
"Deniz yolda giderken bir yere işedi, şimdi oraya Pasifik Okyanusu diyorlar",
"Deniz'i yılan ısırırsa yılan zehirlenerek ölür",
"Deniz sonsuz sayıya kadar sayabilir",
"Deniz araba yarışını kazandı fakat arabayı çalıştırmayı unutmuştu",
"Deniz her gün yaptığı şeyleri bir kitaba not ederdi, şimdi ona rekorlar kitabı deniliyor",
"Deniz evinize gelirse siz misafir olursunuz",
"Cinler Deniz'i 5 harfli diye çağırır",
"Deniz kendi cenazesinde imamlık yapabilir",
"Cinler Deniz'in olduğu eve girmeye korkar",
"Deniz kendi doğumuna doktor olarak katılmıştır",
"Hayaletler kamp ateşi etrafında Deniz hikayeleri anlatırlar",
"Deniz'in geçirdiği 15 ameliyatın 16'sı başarılı oldu",
"Deniz kel bir adamın saçını tıraş edebilir",
"Deniz ayakları yerdeyken havada durabilir",
"Deniz bir gün çöle gitmiştir, susadığı için kumu suya çevirmiştir",
"Bir zombi Deniz'i ısırırsa zombi, Deniz'e dönüşür",
"Einstein atomu parçalarken Deniz'den yardım almıştır",
"Deniz şınav çekmez, dünyayı yukarı aşağı oynatır",
"Deniz 7 kere intihar bombacılığı yapmıştır ve hepsinde başarılı olmuştur",
"Deniz kışın dışarı çıkmıştır, bir süre sonra kar üşümeye başlamış",
"Tekerlek ilk bulunduğunda, Deniz incelemeye giderken arabayla gitmiştir",
"Deniz kardan adam yapmaz, kar onu görünce adam olur",
"Deniz'in eline cam batarsa cam kanamaya başlar",
"Deniz'in ayağına paslı çivi batmış, çiviye tetanoz aşısı yapılmıştır",
"Ateş ilk bulunduğunda Deniz mangal yapıyordu",
"Güneşli havada Deniz dışarı çıkarsa Güneş Deniz'den korunmak için güneş gözlüğü takar",
"Deniz ormanı terk ettikten sonra ormanın kralı aslan olmuştur",
"Araba ilk bulunduğunda Deniz tofaşıyla drift atıyordu",
"Deniz Bülent Ersoy'la bilek güreşi yapar, kaybeden cinsiyetini değiştirecekti",
"Thor'un çekici Deniz'e layık olamadığı için değişmiştir",
"Canavarlar uyumadan önce yatağının altında Deniz var mı diye bakarlar",
"Deniz 2 gün okula gitmemiştir, o günler cumartesi ve pazardır",
"Deniz virüsünü ilk kapan koronadır",
"Deniz uçmaz, hava onu kaldırır",
"Deniz üçlü prize kendi kablosunu takıp enerji üretebilir",
"Deniz koşarken yüzüstü yere düşmüştür. Sikinin değdiği yer Mariana Çukuru olarak bilinmektedir",
"Deniz ölmez, öbür tarafı ziyaret etmeye gider"
]

floods = [
"abooov harbi fişeqsin qardeşm yasal uyarı: bu uyarı t.b.m.m tarafından karara alındı ve saqlık bakanlıqı tarafından onaylandı t.c yasasının 6363 maddesi qereqince'' şeker hastalarının bu resme bakmaları yasaklandı.. çünkû bu resimde %100 şeker orani %100 tatlılık belırlendi ' neyse demek istedqım anlaşıldı galıbaa ayrıca:= o duruşa, bakışa ölünür qnqi senı daha fzla anlatmak isderdım ama sn anlatılmaz'sınnnn (nokta) for alsam ii olacaq lèàn ßù nèè ¤ dùnyàyà mètèør dùsmùşş # àyàqtà ùyùyøz hàßèrìmìz yóúqh ¿¿ phòtòyà qèlìncèè tù tù tù tù # màsàllàhh ànàlàr nè prensesler dôqùrùy ßòylèèèèè ! ßhèn shènïn òóó # sàchına òóò # ßasınaâ òòò # qàşìnààà ôóø # qòzùnèè òøó aşk oldum # duruşuna # süpersn nèysè fazlâ ùzatmîm şekilsin dinimè imanıma yaşlı babama ésrarcı dédémé jilétçi nénémé éroyinci halama n4rkozcu yénqémé müslümcü téyzémin ü$érine yémin édérimqi; çoq qü$él olmuş.'. na$ar déymé$in amin:بِسْمِ اللهِ الرَّحْمنِ الرَّحِيمِوَوَصَّيْنَ الْإِنسَانَ بِوَالِدَيْهِ حُسْنً وَوَصَّيْنَا الْإِنسَانَ بِوَالِدَيْهِ حُسْناً وَإِن جَاهَدَاكَ لِتُشْرِكَ بِي مَا لَيْسَ لَكَ بِهِ عِلْمٌ فَلَا تُطِعْهُمَا إِلَيَّ مَرْجِعُكُمْ فَأُنَبِّئُكُم بِمَا كُنتُمْ تَعْمَلُون ",
"komedi amk boşluğuma geldiii knkkk :joy::joy::100::joy::100::joy::blush::ok_hand_tone2::ok_hand_tone2::100::joy::relaxed::relaxed::relaxed::joy: sjsjsjsj boşluğuma geldi amkkk :joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy: sjsjsjsjdkcjdjsksj olum boşluğuma geldi naptın la :smiley::smiley::grinning:merdim molsun :crying_cat_face::person_pouting::police_officer:madehler molsun:wine_glass::wine_glass::beers: men maybederqen:gun::bomb::knife: mazrail:japanese_goblin::japanese_ogre: meyre mursun:eyes:minliyorsun:ear: mörmüyorsun:see_no_evil:murban:cow2: mederler mimlerle meziyosun :couple::couple::two_men_holding_hands::couple::couple_with_heart:maç mehennem:fire::boom: möndü:sweat_drops: miçimde milmiyorum:question::grey_question: meli :person_wearing_turban:manıyorlarmeni mariyorlar:scream:mörenler:eyes::eyes: mar mı:grey_question:müşen:arrow_heading_down: mu maprağım:leaves::maple_leaf: mençliğimin:boy: müyasıymıs:zzz::zzz:magıda maza maza:pencil::page_with_curl::pencil2:",
"komik:joy::joy: lan:blush::blush: amk:joy::joy::joy: çocukları :joy::joy::joy:buna:joy::joy: gülmeyen :joy::joy:orosbu:joy::joy::joy::joy: çocuğudur :joy::joy::joy::joy: sjsjsjs:joy::joy: kanka :joy::joy::joy:sen:joy::joy: tam:joy::joy: bir:joy::joy: mizahşörsun:joy::joy: aga:joy::joy: krala :joy::joy:bak tespit :joy::joy:gibi:joy::joy: tespit:joy::joy::joy: sen:joy::joy::joy: sakalarini :joy::joy:yiyim :joy::joy:senin:joy::joy: lan :joy::joy:adammm:joy::joy: bunu :joy::joy::joy:komik:joy::joy: bulmayan:joy::joy: 715362:joy::joy: orosbu:joy::joy: evladiini etiketle:joy::joy: hayırlı olsun teşekürler :joy::joy: jöh:joy::joy: pöh :joy::joy:fbı:joy::joy: cıa:joy::joy: mit:joy::joy: derin devlet:joy::joy: sağcılar:joy::joy: solcular:joy::joy: ronaldocular:joy::joy: messiciler:joy::joy: laikler :joy::joy:şeriatçılar :joy::joy:kyk:joy::joy: gkydekiler:joy::joy::joy: uzaylilar :joy::joy::joy:dunya duzculuer:joy::joy: donald trumpcilar:joy::joy: hillary clintoncilar :joy::joy:kim jon un:joy::joy: ben 10 cular :joy::joy:bakuganciler :joy::joy:doğu bloğu:joy::joy: bati blogu :joy::joy:kvp ciler:joy::joy: polat alemdar:joy::joy: hüsnü coban:joy::joy: mesut komiser:joy::joy: jony sins :joy::joy:ulu önder recep tayyip erdoğan hazretleri fanlari :joy::joy:ekrem imamoğlu fanlari:joy::joy: enes batur fanlari:joy::joy: barış ozcan:joy::joy: fanlari malatyalilar:joy::joy: bolulular:joy::joy: sivaslılar :joy::joy:türkler:joy::joy: kürtler:joy::joy: suriyelilet:joy::joy: yunanlar :joy::joy::joy::joy:marslilar:joy::joy: mikroskobik canlilar:joy::joy: hayvanlar:joy::joy: bitkiler:joy::joy: pkklilar:joy::joy: dhkpcliler:joy::joy: burkina fasolular:joy::joy: gambiyalilar:joy::joy: kaptan amerika:joy::joy::joy: iron man :joy::joy:thor:joy::joy: loki :joy::joy:thanos:joy::blush: nebula :joy::joy:natasha :joy::joy:ant man:joy::joy: spiderman:joy::joy: batman:joy::joy: superman supergirl:joy::joy: aquaman :joy::joy:dr manhattan:joy:",
":rolling_eyes:mimimizah şhow:ok_hand::ok_hand::ok_hand::thumbsup::scream::scream::scream::scream::scream::scream::scream::scream::scream::scream::scream::smiley::smiley::smile::smiley::grin::smiley::grin::smiley::grin::grin::smiley::grin::smiley::scream::grinning::grinning::scream::grinning::grin::grinning::scream::rage::scream::grinning::grin::grinning::laughing::grin::laughing::grin::grinning::grin::grinning::grin::grinning::scream::laughing::scream::laughing::grin::laughing::grin::grinning::grinning::grin::grinning::grin::grinning::grin::smile::smiley::scream:ohaaaaa kanka ayyynııı bııızzzz:scream::scream::scream::scream::scream::scream::scream:buna gulucek 930393038392829272837 orospu evladı dostunu etıketle shshsjsjsjsjsjsjsjsjjsjsjsjjsjsjsjsjsjsjsj:ok_hand::ok_hand::ok_hand::ok_hand::smile::smiley::grin::grinning::grin::star2::grin::grinning::grin::smiley::grin::smile::grin::smiley::grin::smiley::grin::smiley::grin::smiley::grin:sjsjsjsjsjsjsjsjsjsjsjssjjssjj:joy::joy::joy::joy::joy::joy::joy::joy::joy:mizah şelalesinden bır yudum aldımdjdjsjsjsj:joy::joy::rofl::rofl::joy::joy::100::100::100::rolling_eyes:mimimizah şhow:ok_hand::ok_hand::ok_hand::thumbsup::scream::scream::scream::scream::scream::scream::scream::scream::scream::scream::scream::smiley::smiley::smile::smiley::grin::smiley::grin::smiley::grin::grin::smiley::grin::smiley::scream::grinning::grinning::scream::grinning::grin::grinning::scream::rage::scream::grinning::grin::grinning::laughing::grin::laughing::grin::grinning::grin::grinning::grin::grinning::scream::laughing::scream::laughing::grin::laughing::grin::grinning::grinning::grin::grinning::grin::grinning::grin::smile::smiley::scream:ohaaaaa kanka ayyynııı bııızzzz:scream::scream::scream::scream::scream::scream::scream:buna gulucek 930393038392829272837 orospu evladı dostunu etıketle shshsjsjsjsjsjsjsjsjjsjsjsjjsjsjsjsjsjsjsj:ok_hand::ok_hand::ok_hand::ok_hand::smile:",
"dürüst olmak gerekirse, benim naçizane görüşüm, tabii ki benim bakış açısından farklı düşünen kimseyi rencide etmeden, ama aynı zamanda bu konuyu farklı bir bakış açısı ile değinmeye çalışarak ve benim gibi her birinizin geçerli fikrini göz önüne alarak gerçekten ne söylemek istediğimi unuttuğumu düşünüyorum",
"çekip gitti dimi olum arkasına bakmadan çe- gibtir olup gitti dimi olum gibtir olup gitti. kandırma lan kendini sevmedi olum seni, canın acıo biliorum, şurası dimi biliyorum olum biliorum, gözaltların mosmor olum görüorum. aynanın karşısına geçip kendine acıosun dimi ayakta duramıosun lan, dizlerin çok acıyo olum biliorum",
"bak simdi kardesim vücut konusunda asla yalan konuşmam konusursam aha su masadaki ekmek carpsin bak simdi sende ki kol ramboda yok ama çalışmıyorsun biraderim halbuki calismamana ragmen sik bakiyim allahh bune be olum sen calissan serefsizim beni bile gecersin belki bi kanat ver ver abim kanat allahina kurban olayim be sirt don heyt aslanim benim senin soyle bir kaba hesaplamayla yag oranin %10 falan bunlari yakicaksin kardesim ben sana efsane bir program yazıcam simdi onu uygulicaksin 1 aya ne 1 ayi 1 haftaya abin gibisin",
"düşünsene birtanem, bir gün kavga ediyoruz, çok kırıyoruz bir birimizi sen kızıyorsun, 1-2 gün bana yazmıyorsun, 3,gün yazmak için duvarıma bakıyorsun, ve duvarımdaki yazılar dikkatini çekiyorr, herkes aynı seyı yazmış ; mekanı cennet olsun, söylesene birtanem , o zaman ne yabacaksın?",
"animeçi olmaak nasıl ßiir duyqu anlatayım sanaa . . ! _ animeçi olmaak 6 yaşındaan itißaren sorulaan türkçee soruyaa 'dai jobu da yo' demektir. 7 yaşındaan sonraa anadildeen koparılıp yarım yamalakk japoncaya zorunlu kalmaktır. açlıqı kimsesizliqi fakirliqi zorluqu gurßetii yaşamaktır. animeçi olmak tokyo gißii ßiir şehirdee polis tarafındaan çewirilip kimliqi sorqulamaktır. ßen turqceemi istiyorum dediqi içiin nezaharetlerdee işkencee görmektir. animeci olmaak işkencee edilirken otakuyuz amk demektir. lisedee dersanedee otobüstee forumlardaa katledilmektir. animeci olmaak zindaan köşelerindee sızlayaan yaralarıylaa animeciliği we otakuculugu haykırmaktır...animeci olduqum için rahatsız olanlar werdiqim rahatsızlıktan dolayı gurur duyuyorum . .",
"laaaaaaaaaaaan sevgilim var allah çarpsın var sevgilim oldu laaaaaaaaaaaaaaan olm şoklardayım ilk defa 20 yıl sonra ananı sikeyim oldu laaaaaaaaaaaannnnnnn yemin ediyorum oldu mutluluktan ağlyorum olm tipimi sikeyim nasıl oldu oha hala inanmıyorum amk dedi be evet be kıza adak falan adıyıcam bekle kartvizit yapptırıcam bu benim sevgilim dövmesi yaptırıcam yeminle yaptırıcam olm kıza allah razı olsun dedim nasıl güldü bana güldü lan evetttttttttt oğlum kız onu ellememe izin verdi bildiğin memesi var lan ilk defa dokundum lan böyle muhteşemdi böyle bacağına dokunuyorum ses çıkarmıyo olm kız be anneme kızı gösterdim ağlıyo şuan teyzemi aradı sevgili olmuş diyo yemek vericekler amk herşeyi var lan kol bacak memesi falan full paket ama ürkütmem ona narin davrancam olm sevgili be olley beeeeee allahım şükürler olsunnnn",
":100: Roblox الله مضحك الجنس Allah Calling الروبوت نيغا Peter Griffin Funny Sex (Allah) :scream::cold_sweat:نيغا الأغنام HAHAHA:woozy_face::woozy_face: :neutral_face::lying_face: Allah Sex Funny :hot_face::hot_face::hot_face::face_with_symbols_over_mouth::face_with_symbols_over_mouth: Gay الأقواس نيغا :nauseated_face::nauseated_face: bruh funny :sob:   Like button رقائق cackle :drooling_face::sweat: Korea :zany_face: ALLAH :hot_face::flushed::smiling_face_with_3_hearts: نيغا سخيفة :joy: Allah sex free haram download 2020 حصن فريق الغش القزم المضحك :gun::gun::gun::firecracker::firecracker::firecracker::crossed_swords::pill::pill::pill::key::key::key:free ram lil uzi has corona cuz he is hate allah free punjabi coronavirus cure no virus :joy::joy::joy::joy: allah bruh nigga cat taylor swift hijabi :flag_pk::flag_pk::flag_pk::flag_pk:",
"adi bakalııım:palms_up_together: hocam mucize arıyoruz:mag: wow :astonished:ne :question:iki defa walkout:astonished: arjantin:flag_ar: noluyo lan:thinking: laan :angry:noluyo laan:thinking: nnneeee:astonished: nnnneee:astonished: hahahahahauuuuuuuvv :joy:nnneee:astonished: arkadaşlar bu şşa-kamera :movie_camera:şakası mı:thinking: nnneeee:thinking: nneee:thinking: messi mi :wheelchair:dandik bir paketten:package: messi mi:wheelchair: dandik bir paketten:astonished: messi mi:wheelchair: ooohhaaa:anguished: ooohhaa:anguished:",
"siz belki bu yorumu kötüliceksiniz ama ben şimdi içimi dökeceğim. o dalga geçtiğiniz onur cimke varya hepinizden 5 10 kat daha akıllı. sanalda şakasına böyle takılıyor gebze fen lisesinde şu an ortalaması 99.3 ve okul 3.cüsü. 2. 99.4 1. 99.6 ve girdiği sınavlarda hastaydı. teogda ilk 400e girdi. 6 farklı dil biliyor ulan 6! ingilizce, ispanyolca, rusça, italyanca, çince. annesi ve babası doktor. her gün farklı rus kız değişiyor. siz onu cılız birşey zannediyosunuz ama vücudunun 1/3'ü kas. bide o kadar ders içinde fortnitedan dünyanın parasını kaldırıyor. kocaelinde çok ünlü. her gün 5 rekat namaz kılıyor. heumrage ile de arkadaş diye biliyorum ben. kısaca siz onur cimke ile dalga geçmeye devam ederken o ayt tyt kasıp doktor olucak. 8 9 yıl sonra götünü yalarsınız artık :d :d",
"""NEDENN ELLERİNDEE KELEPÇEE VARR ?:yellow_heart:
+ KÜRDÜMM DİYEE :heart:
- KULLAĞINDAKİİ KANN NEE ?:green_heart:
+ AHMETT KAYAA DİNLEDİM DİYEE :yellow_heart:
- YAA ELLERİNN NİYEE PARCALANMIŞŞ ?:heart:
+ßAYRAGIMII YERDENN KALDIRDIMM DİYE:green_heart:
- YAA AYAKLARINN ?:yellow_heart:
+ ÖZGÜRLÜĞEE YÜRÜYORUMM DİYEE:heart:
- YAA ETRAFINIII KUŞATANN 3 ZALİMM:green_heart:
+ 3 YANLIŞŞŞ BİR DOGRUYU GÖTÜRÜYORMUŞ:yellow_heart: DİYEE...:heart:
:heart::green_heart:
EĞER KÜRTSEN :yellow_heart::heart::green_heart:KOY
EĞER KÜRT OLUPTA KOYMUYOSAN SEREFSIZSINDİR""",
"""Çal keke çal.
Okul bahçesinde bir gün geziyordum,
Hoca çağırdı 'Mehmet buraya gel.'Buyurun hocamDedi 'Çıkar kalem.Belimden 7.65 çı
kardım.
Dedi 'Çıkar defter.Mahkeme kağıtlarını çıkardım.
Dedi 'Çıkar harita.İşte güzelim orada senin benim vücudumda bıraktığın,
Üç beş tane jilet yarası var ya,
İşte onları çıkardım
Hoca dedi 'Bunlar ne?Hocam üç beş jilet yarası,
Sanki sanırsınız ki psikopatın Allah'ı.
Ama bilmezsiniz ki o üç beş jilet yarası,
Ela gözlü sevdiğimin hatırası.
Çal keke çal.""",
"Hala babasını dowmemis koylu yobazlar warmı? Moruk aykırı olucaksın kolesi deyilsin ya?? Ben ilk dowdugumde yedinci sınıfdayım partiden gelmisim gece saat iki kapiyi actigim gibi nerdesin lan yawsak diye bagirdi dedim sana ne lan kahbe ewladı yuzune bile bakmadim odama yuruyorum ama babam eski komandolardan biliyorumki sinsice yaklasip arkamdan saldiracak tabi ben de uc sene orman muhafizligi egitimi almisim siyah kusagim moruk bir ses kastim tam vuracakken aniden donup bilegini buktum sss geri bas lan geri bas diye bagirdim ne arkadan yaklasiyosun lan dedim tabi o sirada iyice bilegini bukuyorum kivraniyor abi cekmeye basladi ama acimadim amin cocuguna kirilana kadar cevirdim aglamaya basladiginda biraktim ambulansi bile aramadim gittim uyudum babamin amina ilk boyle koydum tavsiye isteyecek olursa sonrasinda uyumayin ben sabah hastanede uyanmistim uykumda bicaklamis orosbu cocugu",
"KUZE CİYA TENYO KARO PEZEVENK HARE VALLA LAY ŞERREFSİZ OĞLU ŞERREFSİZ NUMARAYİ YOLLAYİ LAN BANA AMINA KOYDUM ÇOCUĞU NUMRANI YOLLA NUMARANI HÜSEYİN MEMLEKETİNE GÖMERİM HA SENİ ŞEREFSİZ KİMSİN LAN SEN?",
"BuMm :bomb::boom: TaTLı Mı :smiling_face_with_3_hearts::stuck_out_tongue_winking_eye: cRinGe Mi :zany_face::woozy_face: tAtLı Mı :yum: tAtLı mI :heart_eyes_cat: CrİNgE Mi :scream::persevere: saNaNe :face_with_raised_eyebrow::interrobang: LAnn :bangbang::sunglasses: eLaNuR :eye: BeLa :woman_vampire: kAfALaR :exploding_head: feNa :dizzy: gÖzLeRiM :eyes: eLa :eye: eY :kiss::tongue: dErDiN :face_with_raised_eyebrow: nE:question:sEnİn :point_left:bELa :woman_vampire: Mı İsTiYoN :ghost: BeLa :smiling_imp: mI bELa :skull: yA :call_me:tWiTcHdE :space_invader: bEla :imp: vArDıR oNuN :point_right: aDı eLaDıR :eye: eLA :eyes: Ya :lips:dErDiN :face_with_raised_eyebrow: nE :question: sEnİn :point_left:bELa :skull: Mı İsTiYoN :woman_vampire: BeLa mI :smiling_imp: bELa :ghost: yA :tongue:TwİtChDe :space_invader: BeLa :imp: VaRdIr OnUn :point_right: ADı eLa :eye: Ey :call_me::lips: BuMm :bomb::boom: TaTLı Mı :smiling_face_with_3_hearts::stuck_out_tongue_winking_eye: cRinGe Mi :zany_face::woozy_face: tAtLı Mı :yum: tAtLı mI :heart_eyes_cat: CrİNgE Mi :scream::persevere: saNaNe :face_with_raised_eyebrow::interrobang: LAnn :bangbang::sunglasses: eLaNuR :eye: BeLa :woman_vampire: kAfALaR :exploding_head: feNa :dizzy: gÖzLeRiM :eyes: eLa :eye: eY :kiss::tongue:",
"HOTWEELS ARABAN SHARKYDEN KURTULABİLİR Mİ SENİ CANLI CANLI YUTAR ĞĞAĞHĞAHĞĞĞ BİR DAHA DENE SENİ ŞANSLI ARABA FIRLAT AĞHĞĞĞĞĞH BU ACIDI IAAAĞĞĞĞĞĞĞH İŞTE BUNA KAZA DERİM HOTWHEELSTAN ÇILGIN SHARKY SAHİLDE",
"Boşluğuma geldiii knkkk :joy::joy::100::joy::100::joy::blush::ok_hand_tone2::ok_hand_tone2::100::joy::relaxed::relaxed::relaxed::joy: sjsjsjsj boşluğuma geldi :joy::joy::joy::joy::joy::joy::joy::joy::joy::joy::joy: sjsjsjsjdkcjdjsksj olum boşluğuma geldi naptın la :smiley::smiley::grinning:MeRdiM MolSuN :crying_cat_face::person_pouting::police_officer:MaDehLeR MolSuN:wine_glass::wine_glass::beers: MeN MaYbEdeRQeN:gun::bomb::knife: MaZrAiL:japanese_goblin::japanese_ogre: MeYrE MuRsUn:eyes:MiNliYoRsUn:ear: MörMüYoRsUn:see_no_evil:MuRbAn:cow2: MeDerLeR MiMlErlE MeZiYosUn :couple::couple::two_men_holding_hands::couple::couple_with_heart:MaÇ MeHenNeM:fire::boom: MöNdÜ:sweat_drops: MiÇiMdE MiLmiYoRum:question::grey_question: MeLi :person_wearing_turban:MaNıYorLarMeNi MariYoRlaR:scream:MöReNLer:eyes::eyes: MaR Mı:grey_question:MüŞeN:arrow_heading_down: Mu MapRaĞıM:leaves::maple_leaf: MenÇliĞimİn:boy: MüYasIyMıs:zzz::zzz:MaGıDa MazA MaZa:pencil::page_with_curl::pencil2:MaSrEtiM MeyAza:hourglass_flowing_sand::hourglass:MarArI MerMisTiM MeN:100: MelLeRiMse ManLıYmıs:police_officer:MaNRı:imp: MurDu MaZa :postal_horn:MöLmEdEn:skull:MezArA:wedding::bouquet:Sjsjsjsjssj :wink::joy::joy::joy::joy::joy::joy::joy::joy: HACI KOP KOP DEVİR KOPMA DEVRİ:wink::wink::wink::wink::wink::smiling_face_with_3_hearts::smiling_face_with_3_hearts::smiling_face_with_3_hearts: Buna gülecek 72839393722262 arkadaşını ETIKETLE JSJSKSKS :innocent::innocent::innocent:KANKA AYNI SEN :lips::lips::lips: Amg HOrt lenn:zany_face::zany_face::zany_face: Meler askerim zoruları alam :wink::wink::lips::sunglasses::sunglasses: BİR Zevda ulen Maog,:face_with_symbols_over_mouth::exploding_head::flushed::hot_face:#AMG tuTTuR bAbAağĞ :grinning::wink::wink::heavy_check_mark: #HoRTunAKuweTAMG #HorTlaTSayFaYaÇıKaRTuTaRsaİsMim GözükMesin :100::100::ok_hand::ok_hand:EfSo Mizah MüKeMmEn:gun::gun:A",
"DÜTTT DÜÜÜÜTT AÇ YOLU AÇÇ HADİ ASLAN PARÇASI YOLU AÇ HADİ BAK ENGELLİ BEKLİYO BURDA HADİ DÜÜÜT :wheelchair: BAK SİNİRLENDİ ARKADAŞ HADİ YOLU AÇ HADİ DÜÜÜÜÜT DÜÜÜÜT BİİİPPP :wheelchair::wheelchair: BAK HIZLANDI ENGELLİ KARDEŞİMİZ SERİ KÖZ GETİR SERİ DÜÜÜÜT DÜÜÜT DÜÜÜÜÜÜTTTT BİİİİPP BİİİİİİİİPPPPP DÜÜÜÜTTT :wheelchair::wheelchair::wheelchair::wheelchair: BAK ARTIYO SAYILARI AÇTIN MI YOLU AÇMADIN PÜÜÜ REZİİİİL DÜÜÜÜÜÜTTT :wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair: BAK KALABALIKLAŞTI BAK DELİ GELİYOR DELİRDİ DELİ AÇ YOLU DÜTDÜTDÜTDÜRÜRÜDÜRÜDÜÜÜTTT :wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair::wheelchair: KAFAYI YEDİ BUNLAR AÇ LAAAAN YOLU !",
"hadi bakalııım:palms_up_together: hocam mucize arıyoruz:mag: wow :astonished:ne :question:iki defa walkout:astonished: arjantin:flag_ar: noluyo lan:thinking: laan :angry:noluyo laan:thinking: nnneeee:astonished: nnnneee:astonished: hahahahahauuuuuuuvv :joy:nnneee:astonished: arkadaşlar bu şşa-kamera :movie_camera:şakası mı:thinking: nnneeee:thinking: nneee:thinking: messi mi :wheelchair:dandik bir paketten:package: messi mi:wheelchair: dandik bir paketten:astonished: messi mi:wheelchair: ooohhaaa:anguished: ooohhaa:anguished:",
"Babayın ismini mi söylüyon ZOMBALA BOMBALA HAKUNA MATATA AMUDA KALDIRAGA ZiMBABVE NiJERYANE DANS UZMANI KiM JONG UN BACISINA KALKAN TRUMP IN AMCASININ OĞLU BLADE iN YEĞENi CEZALANDIRICI 7T TERMiNATÖR TURBO TONY TUTANKAMON TANER TOLGA TARLACI METERiN HEM ARKADAŞI HEM DE AYNI ZAMANDA BiR NUMARALI DÜŞMANI KAFES DÖVÜŞÜ UZMANI FLOYD VE MC GREDOR UN BiR NUMARALI DÜŞMANI FBI AJANSI YANGINDA 150 kişiyi kurtaran aynı Zaman'da halk kahramanı SURVIVOR şampiyonu Kıbrıs Girne Amerikan Üniversitesi mezunu 4 y",
"""░░░░░░▄▄▄░░▄██▄░░░
░░░░░▐▀█▀▌░░░░▀█▄░░░
░░░░░▐█▄█▌░░░░░░▀█▄░░
░░░░░░▀▄▀░░░▄▄▄▄▄▀▀░░
░░░░▄▄▄██▀▀▀▀░░░░░░░
░░░█▀▄▄▄█░▀▀░░
░░░▌░▄▄▄▐▌▀▀▀░░ THIS IS BOB
▄░▐░░░▄▄░█░▀▀ ░░
▀█▌░░░▄░▀█▀░▀ ░░ COPY AND PASTE HIM,
░░░░░░░▄▄▐▌▄▄░░░ SO, HE CAN TAKE
░░░░░░░▀███▀█░▄░░ OVER THE WORKSHOP
░░░░░░▐▌▀▄▀▄▀▐▄░░
░░░░░░▐▀░░░░░░▐▌░░
░░░░░░█░░░░░░░░█░░░
░░░░░▐▌░░░░░░░░░█░░"""
]

musics = [
"https://open.spotify.com/track/3eQYcPJLkQUDnxX72TamlZ?si=x9gbjrfTRg6T_NAAJg_eFA",
"https://open.spotify.com/track/0MC6LfBcq3EgLMThwvpZHj?si=zXGnbob9Q9C2B1o38up_ig",
"https://open.spotify.com/track/6mcxQ1Y3uQRU0IHsvdNLH1?si=UXjH8tKWRY6dmFaZGqLUQw",
"https://open.spotify.com/track/4jNQkWhuzqrbqQuqanFFJ6?si=M-j4sX_DTK-XxeBXP61bsw",
"https://open.spotify.com/track/2zYzyRzz6pRmhPzyfMEC8s?si=RNuc6mZnRM-YMNmAL06tdw",
"https://open.spotify.com/track/7iN1s7xHE4ifF5povM6A48?si=HkLLGCjwR_GeSMNGMfAz-g",
"https://open.spotify.com/track/0E3YR9YKrVtfMSUsfBCP9f?si=34alnvr8SKqhYGLku7FwBQ",
"https://open.spotify.com/track/42idQeun2SugRkVxgvBXIb?si=SXBqKhvxRRi3lmB5Gv68EA",
"https://open.spotify.com/track/6Hv48rz1QTiAKARRmYWzi1?si=Lu1wLrPVSn6Vr6XPlYxZ1g",
"https://open.spotify.com/track/19cxPUMbttLsZhifmpKnId?si=XLbdra21Q0GwUpX6pUFAgw",
"https://open.spotify.com/track/4OlblKsdv6FLuWyhB7qnwt?si=PyjL0zjFRge7WoDlwFEP2w",
]

tavsiyeler = [
"Koşarken Memeleriniz Değil Taşaklarınız Sallansın",
"Racon Değil, Kafa Kesin",
"Seks Partneriniz Sıra Bende Derse Kaçın"
]

olasilik = [
"evet",
"hayır"
]

yazi_tura = [
"Yazı",
"Tura"
]

comedy = [
"31 HAHAHAHAHAHA",
"PİPİ ASDJASDHASFKASH",
"YİĞİT OSSURDU HEMİ DE YAYINDA SASKDJASDHJASDBKASJ",
"HEPSİNİ ALIRLAR DİYE SÜNNET OLMAMIŞ METEHAN ASDJKBALSKDBASK"
]

olcu = [
" cm",
" mm",
" mm"
]

rsp = [
"Taş",
"Kağıt",
"Makas"
]

yuzde = [
5,
10,
15,
20,
25,
30,
35,
40,
45,
50,
55,
60,
65,
70,
75,
80,
85,
90,
95,
100
]

databases = [
"akif_sohbet.txt",
"arda_sohbet.txt",
"berkan_sohbet.txt",
"bora_sohbet.txt",
"canberk_sohbet.txt",
"deniz_sohbet.txt",
"efe_sohbet.txt",
"h_gazi_sohbet.txt",
"kaan_sohbet.txt",
"metehan_sohbet.txt",
"mmd_sohbet.txt",
"onur_ata_sohbet.txt",
"slash_sohbet.txt",
"stacker_sohbet.txt",
"yiğit_sohbet.txt",
"yunus_sohbet.txt"
]

menu = """
**```diff
- dm!denizmucizesi 
- dm!deniztavsiyesi
- dm!espri
- dm!flood
- dm!am
- dm!döviz
- dm!korona
- dm!zaman
- dm!hava
- dm!müzik
- dm!sigara
- dm!efkar
- dm!kaçcm
- dm!evethayır
- dm!bot
- dm!ascii
- dm!yazıtura
- dm!taşkağıtmakas
- dm!avatar
- dm!komikkadın
- dm!konuş
- dm!instagram
- dm!youtube
- dm!adminbilgi
- dm!komutlar```**
"""

def listToString(x):   
	str1 = " "   
	return (str1.join(x))

@bot.event
async def on_ready():
	print("Deniz Online")
	print("İsmim {}".format(bot.user.name))
	print(str(len(set(bot.get_all_members()))) + " Kişiye Kamp Ateşi Etrafında Mucize Anlatıyor!")
	activity = discord.Game(name = "dm!komutlar")
	await bot.change_presence(status = discord.Status.idle, activity = activity)

@bot.event
async def on_message_delete(message):
	kim = message.author
	mesajicerik = message.content
	print("Silinen mesaj => ", kim, ":", mesajicerik)
	await bot.process_commands(message)
	silinenMesaj = mesajicerik.lower()
	if silinenMesaj == "@everyone":
		await message.channel.send("Boşuna Niye everyone attın mal")

@bot.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.author.bot: return

	elif not message.author == client.user:
		mesaj = message.content.lower()
		splitted = mesaj.split(sep = " ")
		isim = message.author
		isim = str(isim)
		parcala = isim.split(sep = "#")
		etiket = parcala[-1]
		etiket = str(etiket)

		if mesaj == "yalancı deniz":
			await message.channel.send("Anan Yalancı")
		
		elif mesaj == "dm!denizmucizesi":
			await message.channel.send(mucizeler[random.randint(0, 87)])
		
		elif mesaj == "dm!döviz":
			dolar_kuru = requests.get('http://bigpara.hurriyet.com.tr/doviz/dolar/')
			soup = BeautifulSoup(dolar_kuru.content, "html.parser")
			dolar_fiyat = soup.find("span", {"class":"value up"})

			euro_kuru = requests.get('http://bigpara.hurriyet.com.tr/doviz/euro/')
			soup = BeautifulSoup(euro_kuru.content, "html.parser")
			euro_fiyat = soup.find("span", {"class":"value up"})

			sterlin_kuru = requests.get('http://bigpara.hurriyet.com.tr/doviz/sterlin/')
			soup = BeautifulSoup(sterlin_kuru.content, "html.parser")
			sterlin_fiyat = soup.find("span", {"class":"value up"})

			await message.channel.send("```1 Dolar " + dolar_fiyat.text + " TL```")
			await message.channel.send("```1 Euro " + euro_fiyat.text + " TL```")
			await message.channel.send("```1 İngiliz Sterlini " + sterlin_fiyat.text + " TL```")
		
		elif mesaj == "dm!am":
			await message.channel.send("**Ohhhh**")

		elif mesaj == "dm!korona" or mesaj == "dm!covid19":
			saglik = requests.get('https://covid19.saglik.gov.tr/')
			soupC = BeautifulSoup(saglik.content, "html.parser")
			test = soupC.find("span", {"class":"buyuk-bilgi-l-sayi"})
			veriler = soupC.find_all("span", {"class":""})
			await message.channel.send("```Bugünkü Test Sayısı {}```".format(test.text))
			await message.channel.send("```Bugünkü Vaka Sayısı {}```".format(veriler[13].text))
			await message.channel.send("```Bugünkü Vefat Sayısı {}```".format(veriler[15].text))
			await message.channel.send("```Bugünkü İyileşen Sayısı {}```".format(veriler[17].text))
		
		elif mesaj == "dm!corona" or mesaj == "dm!2019nCov":
			saglik = requests.get('https://covid19.saglik.gov.tr/')
			soupC = BeautifulSoup(saglik.content, "html.parser")
			test = soupC.find("span", {"class":"buyuk-bilgi-l-sayi"})
			veriler = soupC.find_all("span", {"class":""})
			await message.channel.send("```Bugünkü Test Sayısı {}```".format(test.text))
			await message.channel.send("```Bugünkü Vaka Sayısı {}```".format(veriler[13].text))
			await message.channel.send("```Bugünkü Vefat Sayısı {}```".format(veriler[15].text))
			await message.channel.send("```Bugünkü İyileşen Sayısı {}```".format(veriler[17].text))
		
		elif mesaj == "dm!instagram":
			await message.channel.send("https://www.instagram.com/denizmucizesi")
		
		elif mesaj == "dm!youtube":
			await message.channel.send("https://www.youtube.com/channel/UC70_DJ-HwRCuHjgL8QLyCPQ")

		elif mesaj == "dm!komutlar":
			await message.channel.send(menu)
				
		elif mesaj == "dm!espri":
			await message.channel.send(comedy[random.randint(0, 3)])
		
		elif mesaj == "dm!zaman":
			day = ctime().split(sep = " ")
			if day[1] == "Jan":
				day[1] = "Ocak"
			elif day[1] == "Feb":
				day[1] = "Şubat"
			elif day[1] == "Mar":
				day[1] = "Mart"
			elif day[1] == "Apr":
				day[1] = "Nisan"
			elif day[1] == "May":
				day[1] = "Mayıs"
			elif day[1] == "Jun":
				day[1] = "Haziran"
			elif day[1] == "Jul":
				day[1] = "Temmuz"
			elif day[1] == "Aug":
				day[1] = "Ağustos"
			elif day[1] == "Sep":
				day[1] = "Eylül"
			elif day[1] == "Oct":
				day[1] = "Ekim"
			elif day[1] == "Nov":
				day[1] = "Kasım"
			elif day[1] == "Dec":
				day[1] = "Aralık"
			if day[0] == "Mon":
				day[0] = "Pazartesi"
			elif day[0] == "Tue":
				day[0] = "Salı"
			elif day[0] == "Wed":
				day[0] = "Çarşamba"
			elif day[0] == "Thu":
				day[0] = "Perşembe"
			elif day[0] == "Fri":
				day[0] = "Cuma"
			elif day[0] == "Sat":
				day[0] = "Cumartesi"
			elif day[0] == "Sun":
				day[0] = "Pazar"
			newday = day[2] + " " + day[1] + " " + day[-1]
			days = day[0]
			
			time = ctime().split(sep = " ")
			newtime = time[3]

			await message.channel.send("**Bugün** " + newday + " **Günlerden** " + days + " **Saat** " + newtime)

		elif mesaj == "dm!efkar":
			deger = str(yuzde[random.randint(0, 19)])
			efkar_yuzde = "%" + deger
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + " || " + ":smoking: " + "Efkar Ölçer " + efkar_yuzde + " Efkar Ölçtü " + ":smoking:")
			sleep(5)
			await message.channel.send("Senin ben derdini sikeyim")
		
		elif mesaj == "dm!cugara" or mesaj == "dm!sigara":
			await message.channel.send(":japanese_goblin: :smoking: :cloud: :cloud: :cloud: :cloud:")
			sleep(2)
			await message.channel.send("Sağlığınız İçin Sigara İçin")

		elif mesaj == "dm!yazıtura":
			sonuc = yazi_tura[random.randint(0, 1)]
			await message.channel.send("Bekle Biraz Para Dönüyor...")
			sleep(5)
			await message.channel.send("Sonuç: " + sonuc)

		elif mesaj == "dm!taşkağıtmakas":
			user_choose = rsp[random.randint(0, 2)]
			enemy_choose = rsp[random.randint(0, 2)]
			if user_choose == "Taş":
				if enemy_choose == "Taş":
					await message.channel.send("Seçimin: " + user_choose)
					await message.channel.send("Rakibin Seçimi: " + enemy_choose)
					await message.channel.send("Sonuç: Berabere!")

				elif enemy_choose == "Kağıt":
					await message.channel.send("Seçimin: " + user_choose)
					await message.channel.send("Rakibin Seçimi: " + enemy_choose)
					await message.channel.send("Sonuç: Kaybettin!")

				elif enemy_choose == "Makas":
					await message.channel.send("Seçimin: " + user_choose)
					await message.channel.send("Rakibin Seçimi: " + enemy_choose)
					await message.channel.send("Sonuç: Kazandın!")

			elif user_choose == "Kağıt":
				if enemy_choose == "Taş":
					await message.channel.send("Seçimin: " + user_choose)
					await message.channel.send("Rakibin Seçimi: " + enemy_choose)
					await message.channel.send("Sonuç: Kazandın!")

				elif enemy_choose == "Kağıt":
					await message.channel.send("Seçimin: " + user_choose)
					await message.channel.send("Rakibin Seçimi: " + enemy_choose)
					await message.channel.send("Sonuç: Berabere!")

				elif enemy_choose == "Makas":
					await message.channel.send("Seçimin: " + user_choose)
					await message.channel.send("Rakibin Seçimi: " + enemy_choose)
					await message.channel.send("Sonuç: Kaybettin!")

			elif user_choose == "Makas":
				if enemy_choose == "Taş":
					await message.channel.send("Seçimin: " + user_choose)
					await message.channel.send("Rakibin Seçimi: " + enemy_choose)
					await message.channel.send("Sonuç: Kaybettin!")

				elif enemy_choose == "Kağıt":
					await message.channel.send("Seçimin: " + user_choose)
					await message.channel.send("Rakibin Seçimi: " + enemy_choose)
					await message.channel.send("Sonuç: Kazandın!")

				elif enemy_choose == "Makas":
					await message.channel.send("Seçimin: " + user_choose)
					await message.channel.send("Rakibin Seçimi: " + enemy_choose)
					await message.channel.send("Sonuç: Berabere!")


		elif mesaj == "dm!kaçcm" or mesaj == "dm!muzum":
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			isim = message.author
			isim = str(isim)
			parcala = isim.split(sep = "#")
			etiket = parcala[-1]
			etiket = str(etiket)
			uzunluk = str(olcu[random.randint(0, 2)])
			if etiket == "4243":
				await message.channel.send(son_id + "Big Smoke'un Big Dick'i Olur: 31 cm")
			elif etiket == "0037":
				await message.channel.send(son_id + "'nın Muzu Çok Uzun Olduğu İçin Ölçemiyorum")
			elif etiket == "2711":
				await message.channel.send("Yiğit'in Taşşaklarına Beton Yetmez")
			elif etiket == "3109":
				await message.channel.send("Onur Ata'nın Taşşaklarına Beton Yetmez")
			elif etiket == "1341":
				await message.channel.send(son_id + "'nın Muzu Ölçümlerime Göre " + str(random.randint(0, 5)) + " mm")
			elif etiket == "3478":
				await message.channel.send(son_id + " Senin Muzun Yok Ama Üzülme Çünkü Sen Mükemmel Bir Orospu Çocuğusun")
			else:
				if uzunluk == " mm":
					teselli = " Üzülme Senin Muzun Da Uzar"
				await message.channel.send(son_id + "'nın Muzu Ölçümlerime Göre " + str(random.randint(1, 50)) + uzunluk)
				if uzunluk == " mm":
					await message.channel.send(son_id + teselli)

		elif mesaj == "dm!deniztavsiyesi":
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			tavsiye = tavsiyeler[random.randint(0, 2)]
			await message.channel.send(tavsiye)

		elif "<@718472977959747654>" in mesaj:
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + " Ne var lan yarram")

		elif "<@&718930404681449594>" in mesaj:
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + " Ne var lan yarram")

		elif "<@!718472977959747654>" in mesaj:
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + " Ne var lan yarram")

		elif mesaj == "Mal Deniz" or mesaj == "mal deniz":
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + " Hele yarrama bak")			

		elif mesaj == "MAL DENİZ" or mesaj == "Mal deniz":
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + " Hele yarrama bak")

		elif mesaj == "sa" or mesaj == "SA":
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + ", Allahını S.., AS Kardeş!")

		elif mesaj == "selam" or mesaj == "slm":
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + ", Allahını S.., AS Kardeş!")

		elif mesaj == "ü" or mesaj == "Ü":
			await message.channel.send("https://www.youtube.com/alperenguner")

		elif mesaj == "ban" or mesaj == "BAN":
			await message.channel.send("<:ban:724379478255468595>")

		elif mesaj == "dm!adminbilgi":
			await message.channel.send("Benim Allah'ım: <@!458360309220900874>")
			await message.channel.send("Instagram: https://www.instagram.com/alperen.h265")
			await message.channel.send("Youtube: https://www.youtube.com/alperenguner")

		elif mesaj == "dm!flood":
			await message.channel.send(floods[random.randint(0, len(floods) - 1)])

		elif mesaj == "dm!komikkadın":
			await message.channel.send(file = discord.File("./komik_kadın/{}.jpg".format(random.randint(1,18))))

		elif mesaj == "dm!müzik":
			await message.channel.send(musics[random.randint(0, len(musics) - 1)])

		elif mesaj == "dm!kavga":
			pass

		elif mesaj == "dm!deniz":
			pass

######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################

		if splitted[0] == "dm!evethayır":
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			await message.channel.send(son_id + " " + olasilik[random.randint(0, 1)])

		elif splitted[0] == "dm!avatar":
			if (message.mentions.__len__()>0):
				for user in message.mentions:
					link = user.avatar_url_as(format = None, static_format = "png", size = 2048)
					filename = "avatar" + "_" + str(user.name) + ".png"
					r = requests.get(link, stream = True)
					if r.status_code == 200:
							r.raw.decode_content = True
							with open(filename, "wb") as f:
								shutil.copyfileobj(r.raw, f)
							print("Dosya Başarıyla İndirildi: ", filename)
							await message.channel.send(file = discord.File(filename))
					else:
						print("Dosya Sunucudan Alınamadı")
						await message.channel.send("Dosya Sunucudan Alınamadı")	
			else:
				await message.channel.send("dm!avatar Komutunu Kullandıktan Sonra Boşluk Bırakarak Profil Resmini Görmek İstediğiniz Kişiyi Etiketlemeniz Gerekmektedir")


		elif splitted[0] == "dm!bot":
			user_id = message.author.id
			user_id = str(user_id)
			son_id = "<@!" + user_id + ">"
			son_id = str(son_id)
			with open("./databases/deniz_sohbet.txt", "r", encoding = "utf-8") as f:
				content = [line.strip() for line in f]
			keyword = content[random.randint(0, len(content) - 1)]
			keyword = str(keyword)
			if keyword == "?":
				newkeyword == content[random.randint(0, len(content) - 1)]
				if newkeyword == "?":
					await message.channel.send(son_id + " Mesaj, Veritabanından Çekilemedi")
				else:
					await message.channel.send(son_id + " " + newkeyword)
			else:
				await message.channel.send(son_id + " " + keyword)

		elif splitted[0] == "dm!ascii":
			wordlist = mesaj.split()
			wordlist.pop(0)
			words = listToString(wordlist)
			word = text2art(words)
			if word == "":
				await message.channel.send("dm!ascii Komutunu Kullandıktan Sonra Boşluk Bırakarak Yazdıracağınız Kelimeyi Yazmanız Gerekmektedir")
			else:
				await message.channel.send("```" + word + "```")

		elif splitted[0] == "dm!konuş":
			wordlist = mesaj.split()
			wordlist.pop(0)
			words = listToString(wordlist)
			if words == "":
				await message.channel.send("dm!konuş Komutunu Kullandıktan Sonra Boşluk Bırakarak Bota Söyleteceğiniz Şeyi Yazmanız Gerekmektedir")
			else:
				await message.channel.send(words)

		elif splitted[0] == "dm!userid":
			kisi = splitted[1]
			kisi = str(kisi)
			await message.channel.send("```" + kisi + "```")

		elif splitted[0] == "dm!hava":
			try:
				city = splitted[1]
				if city == "adana":
					city = "9905"
				elif city == "adıyaman":
					city = "41415"
				elif city == "afyonkarahisar":
					city = "11318"
				elif city == "ağrı":
					city = "42230"
				elif city == "aksaray":
					city = "45455"
				elif city == "amasya":
					city = "44254"
				elif city == "ankara":
					city = "18522"
				elif city == "antalya":
					city = "893"
				elif city == "ardahan":
					city = "110688"
				elif city == "artvin":
					city = "41372"
				elif city == "aydın":
					city = "33373"
				elif city == "balıkesir":
					city = "39365"
				elif city == "bartın":
					city = "239809"
				elif city == "batman":
					city = "50677"
				elif city == "bayburt":
					city = "63241"
				elif city == "bilecik":
					city = "56547"
				elif city == "bingöl":
					city = "40464"
				elif city == "bitlis":
					city = "62255"
				elif city == "bolu":
					city = "39884"
				elif city == "burdur":
					city = "42334"
				elif city == "bursa":
					city = "9592"
				elif city == "çanakkale":
					city = "11200"
				elif city == "çankırı":
					city = "41308"
				elif city == "çorum":
					city = "43216"
				elif city == "denizli":
					city = "w277016"
				elif city == "diyarbakır":
					city = "33376"
				elif city == "düzce":
					city = "41688"
				elif city == "edirne":
					city = "53438"
				elif city == "elazığ":
					city = "44812"
				elif city == "erzincan":
					city = "40616"
				elif city == "erzurum":
					city = "1185"
				elif city == "eskişehir":
					city = "33377"
				elif city == "gaziantep":
					city = "11304"
				elif city == "giresun":
					city = "35884"
				elif city == "gümüşhane":
					city = "239500"
				elif city == "hakkari":
					city = "239536"
				elif city == "hatay":
					city = "38896"
				elif city == "ığdır":
					city = "61195"
				elif city == "ısparta":
					city = "50691"
				elif city == "istanbul":
					city = "18319"
				elif city == "izmir":
					city = "18523"
				elif city == "kahramanmaraş":
					city = "37261"
				elif city == "maraş":
					city = "37261"
				elif city == "karabük":
					city = "39097"
				elif city == "karaman":
					city = "53363"
				elif city == "kars":
					city = "55518"
				elif city == "kastamonu":
					city = "47015"
				elif city == "kayseri":
					city = "9913"
				elif city == "kırıkkale":
					city = "62856"
				elif city == "kırklareli":
					city = "40729"
				elif city == "kırşehir":
					city = "48872"
				elif city == "kilis":
					city = "239530"
				elif city == "kocaeli":
					city = "36062"
				elif city == "konya":
					city = "11234"
				elif city == "kütahya":
					city = "37312"
				elif city == "malatya":
					city = "36719"
				elif city == "manisa":
					city = "35887"
				elif city == "mardin":
					city = "39835"
				elif city == "mersin":
					city = "w273216"
				elif city == "muğla":
					city = "33382"
				elif city == "muş":
					city = "112316"
				elif city == "nevşehir":
					city = "33383"
				elif city == "niğde":
					city = "35888"
				elif city == "ordu":
					city = "35889"
				elif city == "osmaniye":
					city = "w273466"
				elif city == "rize":
					city = "16454"
				elif city == "sakarya":
					city = "w270161"
				elif city == "samsun":
					city = "39995"
				elif city == "siirt":
					city = "342789"
				elif city == "sinop":
					city = "45264"
				elif city == "sivas":
					city = "46318"
				elif city == "şanlıurfa":
					city = "16506"
				elif city == "şırnak":
					city = "305244"
				elif city == "tekirdağ":
					city = "35342"
				elif city == "tokat":
					city = "45684"
				elif city == "trabzon":
					city = "26039"
				elif city == "tunceli":
					city = "118076"
				elif city == "uşak":
					city = "45426"
				elif city == "van":
					city = "15481"
				elif city == "yalova":
					city = "w673254"
				elif city == "yozgat":
					city = "97157"
				elif city == "zonguldak":
					city = "40096"
				image_urls = "http://www.mgm.gov.tr/sunum/tahmin-show-2.aspx?m={}&basla=1&bitir=5&rC=111&rZ=fff".format(city)
				image_url = "https://w.bookcdn.com/weather/picture/32_{}_1_21_3658db_250_2a48ba_ffffff_ffffff_1_2071c9_ffffff_0_6.png".format(city)
				filename = "weather.png"
				r = requests.get(image_url, stream = True)

				if r.status_code == 200:
					r.raw.decode_content = True
					with open(filename, "wb") as f:
						shutil.copyfileobj(r.raw, f)
					print("Dosya Başarıyla İndirildi: ", filename)
					await message.channel.send(file = discord.File("weather.png"))

				else:
					print("Dosya Sunucudan Alınamadı")
					await message.channel.send("Dosya Sunucudan Alınamadı")				

			except IndexError:
				await message.channel.send("dm!hava Komutunu Kullandıktan Sonra Boşluk Bırakarak Şehir İsmi Yazmanız Gerekmektedir")

		if etiket == "0037":
			file = open("./databases/alperen_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "4243":
			file = open("./databases/deniz_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "2711":
			file = open("./databases/yiğit_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "3109":
			file = open("./databases/onur_ata_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "8859":
			file = open("./databases/metehan_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "3478":
			file = open("./databases/efe_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "2256":
			file = open("./databases/h_gazi_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "3560":
			file = open("./databases/kaan_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "7459":
			file = open("./databases/bora_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "1565":
			file = open("./databases/yunus_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "7302":
			file = open("./databases/slash_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "1174":
			file = open("./databases/mmd_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "2631":
			file = open("./databases/arda_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "8343":
			file = open("./databases/canberk_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "6202":
			file = open("./databases/berkan_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "1341":
			file = open("./databases/stacker_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "3242":
			file = open("./databases/akif_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

		elif etiket == "9388":
			file = open("./databases/deniz_sohbet.txt", "a", encoding = "utf-8")
			file.write(mesaj + "\n")
			file.close()

bot.run("NzE4NDcyOTc3OTU5NzQ3NjU0.Xtq8DA.ufPioRtnKOCRHYLW13NpzENI-fU")

#<@!718472977959747654>
