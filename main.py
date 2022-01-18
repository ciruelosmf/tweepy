import random
import tweepy
import tweet_thread_function

consumer_key = "T0o63gCDRBWrwP"
consumer_secret="N3GoB"
access_token = "13655463IZUrQ7OrcCEMijcWPtW5PRC8"
access_token_secret = "HwgU78AkT2NU3FGs6MitFBzo6KymJv"
bearer_token = "AAAAAAA2NzxZZcteW5taV9EEj9"

file_name = "list.txt"
list_links = [
    ['https://twitter.com/1DeepNote/status/1476887157218463745'],
 ['https://twitter.com/heyeaslo/status/1477822027507519489'],
 ['https://twitter.com/ApprovedSide/status/1477993934240595972'],
 ['https://twitter.com/WealthInc247/status/1477993016321261575'],
 ['https://twitter.com/Infinitians1/status/1477982830688829441'],
 ['https://twitter.com/investmattallen/status/1478059828778082305'],
 ['https://twitter.com/Camp4/status/1478109994243420162'],
 ['https://twitter.com/Nicolascole77/status/1478120718873341961'],
 ['https://twitter.com/LegacyBuilder8/status/1478120958418472960'],
 ['https://twitter.com/wealth_director/status/1478214606686359556'],
 ['https://twitter.com/AlexAndBooks_/status/1478185476850913286'],
 ['https://twitter.com/Philosophy_DQ/status/1477952254187606017'],
 ['https://twitter.com/1DeepNote/status/1478337038113988611'],
 ['https://twitter.com/UpSkillYourLife/status/1478357789856567298'],
 ['https://twitter.com/SahilBloom/status/1412391311840251904'],
 ['https://twitter.com/heyeaslo/status/1478184415721259008'],
 ['https://twitter.com/SachinRamje/status/1478460139426308096'],
 ['https://twitter.com/ccmarce_writes/status/1478384730626269186'],
 ['https://twitter.com/UpSkillYourLife/status/1478727644099190785'],
 ['https://twitter.com/dailystoic/status/1478446746997035018'],
 ['https://twitter.com/Infinitians1/status/1478707606231285761'],
 ['https://twitter.com/hwbhatti/status/1478718272052678656'],
 ['https://twitter.com/Infinitians1/status/1478707606231285761'],
 ['https://twitter.com/AccentInvesting/status/1478679345384148992'],
 ['https://twitter.com/Mindset_Machine/status/1478713315001921540'],
 ['https://twitter.com/KateBour/status/1478792178726019073'],
 ['https://twitter.com/wise_chimp_/status/1478820187449315329'],
 ['https://twitter.com/1DeepNote/status/1478704022815232003'],
 ['https://twitter.com/1DeepNote/status/1477967926410072065'],
 ['https://twitter.com/1DeepNote/status/1477624360781467649'],
 ['https://twitter.com/1DeepNote/status/1477249472111464450'],
 ['https://twitter.com/LegacyBuilder8/status/1478775322439032847'],
 ['https://twitter.com/1DeepNote/status/1479084563087470594'],
 ['https://twitter.com/Philosophy_DQ/status/1479039313937588230'],
 ['https://twitter.com/wealth_director/status/1479099101870542850'],
 ['https://twitter.com/UpSkillYourLife/status/1479090925913575424'],
 ['https://twitter.com/GrammarHippy/status/1449788356309684231'],
 ['https://twitter.com/0xsash/status/1478712119201726466'],
 ['https://twitter.com/AlexAndBooks_/status/1479166643913768960'],
 ['https://twitter.com/dklineii/status/1479071510010601474'],
 ['https://twitter.com/UpSkillYourLife/status/1479450201047781377'],
 ['https://twitter.com/Mindset_Machine/status/1479437925339205636'],
 ['https://twitter.com/nathanbarry/status/1479463607649792004'],
 ['https://twitter.com/amandanat/status/1479481455990296580'],
 ['https://twitter.com/WealthInc247/status/1479487150114672640'],
 ['https://twitter.com/wise_chimp/status/1479510949249830917'],
 ['https://twitter.com/RomeenSheth/status/1455331061416828929'],
 ['https://twitter.com/businessbarista/status/1415303812466814983'],
 ['https://twitter.com/SahilBloom/status/1456664828320362502'],
 ['https://twitter.com/UpSkillYourLife/status/1479814694172958720'],
 ['https://twitter.com/joe_portsmouth/status/1479829757755752450'],
 ['https://twitter.com/wdmorrisjr/status/1480186297180319744'],
 ['https://twitter.com/WealthInc247/status/1480165468434571269'],
 ['https://twitter.com/CoreyWilksPsyD/status/1479881088889602048'],
 ['https://twitter.com/wise_chimp/status/1480223198742515716'],
 ['https://twitter.com/UpSkillYourLife/status/1480185151044796416'],
 ['https://twitter.com/Deep_thoughtsHQ/status/1475438537495355392'],
 ['https://twitter.com/Infinitians1/status/1473271788637343746'],
 ['https://twitter.com/drewrcarr/status/1468949773948526596'],
 ['https://twitter.com/SahilBloom/status/1467136783083261965'],
 ['https://twitter.com/10kdiver/status/1287043526153273344'],
 ['https://twitter.com/girdley/status/1464269525780766720'],
 ['https://twitter.com/SahilBloom/status/1462428192409591819'],
 ['https://twitter.com/FromValue/status/1305839556483313669'],
 ['https://twitter.com/investing_city/status/1296858815262937088'],
 ['https://twitter.com/chamath/status/1305550186341564417'],
 ['https://twitter.com/patrick_oshag/status/1428811209428586502'],
 ['https://twitter.com/BrianFeroldi/status/1308780530712940544'],
 ['https://twitter.com/StraightLineAd/status/1480235441152536582'],
 ['https://twitter.com/Mindset_Machine/status/1480526658859782145'],
 ['https://twitter.com/LegacyBuilder8/status/1480539972532899840'],
 ['https://twitter.com/wealth_director/status/1478016763057033224'],
 ['https://twitter.com/aaditsh/status/1432369566764634112'],
 ['https://twitter.com/wizofecom/status/1478016106132557826'],
 ['https://twitter.com/OneJKMolina/status/1471132453616197635'],
 ['https://twitter.com/jmikolay/status/1480680006242107392'],
 ['https://twitter.com/AskTheGiver/status/1480941652755767299'],
 ['https://twitter.com/UnleashTheKnow_/status/1374730575421050883'],
 ['https://twitter.com/Motivation_Qu_/status/1480981638746103809'],
 ['https://twitter.com/ApprovedSide/status/1481268318195658752'],
 ['https://twitter.com/chrisxmunn/status/1481251357243834370'],
 ['https://twitter.com/AskTheGiver/status/1481995005816365058'],
 ['https://twitter.com/wise_chimp/status/1482428351340068864'],
 ['https://twitter.com/LegacyBuilder8/status/1482365146119000065'],
 ['https://twitter.com/wise_chimp/status/1483126745603743748'],
 ['https://twitter.com/barrettjoneill/status/1483109483270205440']]



"""
"""
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret, bearer_token=bearer_token
)
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


if __name__ == "__main__":
    tweet_thread_function.make_tweet(client, list_links)
 
