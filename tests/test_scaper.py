from web_scraping.scraper import get_citations_needed_count, get_citations_needed_report

def test_get_count():
    URL = 'https://en.wikipedia.org/wiki/Battle_of_the_Bulge'
    actual = get_citations_needed_count(URL)
    expected = 9
    assert actual == expected

def test_report():
    URL = 'https://en.wikipedia.org/wiki/Battle_of_the_Bulge'
    actual = get_citations_needed_report(URL)[0]
    expected = 'The Wehrmacht\'s code name for the offensive was Unternehmen Wacht am Rhein ("Operation Watch on the Rhine"), after the German patriotic hymn Die Wacht am Rhein, a name that deceptively implied the Germans would be adopting a defensive posture along the Western Front. The Germans also referred to it as "Ardennenoffensive" (Ardennes Offensive) and Rundstedt-Offensive, both names being generally used nowadays in modern Germany.[citation needed] The French (and Belgian) name for the operation is Bataille des Ardennes (Battle of the Ardennes). The battle was militarily defined by the Allies as the Ardennes Counteroffensive, which included the German drive and the American effort to contain and later defeat it. The phrase Battle of the Bulge was coined by contemporary press to describe the way the Allied front line bulged inward on wartime news maps.[38][39]'
    assert actual == expected

