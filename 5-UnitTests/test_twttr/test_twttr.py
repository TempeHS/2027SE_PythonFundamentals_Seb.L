from twttr import shorten


    def test_Lcase_Removal():
        try:
            assert shorten("twitter") == "twttr"
        except:
            print("twitter != twttr")

        try:
            assert shorten("TWITTER") == "TWTTR"
        except:
            print("TWITTER != TWTTR ")
    try:
        assert shorten("CS50") == "CS50"
    except:
        print("CS50 != CS50")

    try:
        assert shorten("What's up?") == "Wht's p?"
    except:
        print("What's up? != Wht's p?")

if __name__ =