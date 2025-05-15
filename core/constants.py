"""
Sammlung von konstanten Textlisten für humorvolle Meldungen und Dialoge in der DAUs42-Anwendung.
Diese Listen werden verwendet, um zufällige, thematisch passende Nachrichten anzuzeigen.
"""

def t(translation, lang, key):
    return translation[lang].get(key, key)

warning_icons = [
    "⚠", "🚫", "💥", "☢", "🧨","💣",
]

button_texts = {
    "de" : {
        "print_internet": "Internet drucken",
        "dau_console": "DAU-Konsole öffnen",
        "ultimate_answer": "Ultimative Antwort generieren",
        "random_excuse": "Zufällige Ausrede",
        "dont_panic": "Don't Panic!",
        "god_mode": "GOD-Mode für Mutige",
        "exit_program": "Programm beenden"
        },
    "en" : {
        "print_internet": "Print internet",
        "dau_console": "Open DAU console",
        "ultimate_answer": "Generate ultimate answer",
        "random_excuse": "Random excuse",
        "dont_panic": "Don't Panic!",
        "god_mode": "GOD-mode for the brave",
        "exit_program": "Exit program"
        }
    }

tooltips = {
    "de" : {
        "print_internet": "Druckt das gesamte Internet auf Recyclingpapier",
        "dau_console": "Für Menschen mit fragwürdigem IT-Wissen",
        "ultimate_answer": "Antwort auf das Leben, das Universum und den ganzen Rest",
        "random_excuse": "Wenn du wieder Mist gebaut hast – blame the Hamster",
        "dont_panic": "Beruhigung für angehende IT-Apokalypsen",
        "god_mode": "Aktiviert nutzlose Funktionen mit Stil",
        "exit_program": "Funktionalität entfernt"
        },
    "en" : {
        "print_internet": "Prints the entire internet on recycled paper",
        "dau_console": "For people with curious IT-knowledge",
        "ultimate_answer": "Answer to the universe, the life and the rest",
        "random_excuse": "If you've messed up again – blame the hamster",
        "dont_panic": "Reassurance for impending IT apocalypses",
        "god_mode": "Activates useless features with style",
        "exit_program": "Functionality removed"
        }
    }



internet_status = {
    "de" : {
        "print_internet_success": "Druck des Internets wurde erfolgreich gestartet.",
        "printer_out_of_paper": "Papier reicht nicht. Versuche, WLAN nachzufüllen...",
        "printout_rhesus_b": "Ausdruck erfolgt wunschgemäß in weißer Rhesus-B-Schrift auf transparentem Papier.",
        "error_404": "Fehler 404 – Tinte nicht gefunden.",
        "print_page_1": "Druckseite 1 von ∞ – bitte warten Sie galaktisch geduldig.",
        "done": "Fertig... in 300.059.316 Jahren.\nSollen wir solange was spielen?"
        },
    "en" : {
        "print_internet_success": "Print of Internet was successfully started.",
        "printer_out_of_paper": "Printer out of paper. Trying to refill WLAN...",
        "printout_rhesus_b": "Printout will be in white Rhesus B font on transparent paper as requested",
        "error_404": "Error 404 – Ink not found.",
        "print_page_1": "Printing page 1 of ∞ – please wait galactically patiently.",
        "done": "Done... in 300,059,316 years. Should we play something in the meantime?"
        }
    }
    
dau_responses = {
    "de" : {
        "become_smarter": "Haben Sie schon versucht, intelligenter zu werden?",
        "click_harder": "Klicken Sie bitte fester. Das hilft bestimmt.",
        "restart_universe": "Bitte starten Sie das Universum neu und versuchen Sie es erneut.",
        "problem_ignored": "Wir haben Ihr Problem ignoriert. Viel Erfolg!",
        "problem_moved": "Ihr Problem wurde in die Rundablage verschoben.",
        "dau_detected": "DAU erkannt – Sarkasmus wird hochgefahren...",
        "turn_off_device": "Schalten Sie das Gerät aus und denken Sie über Ihre Entscheidungen nach.",
        "cant_open_dau_console": "Konnte DAU-Konsole nicht öffnen. Daten-Überlauf im WLAN-Kabel.",
        "tried_with_towel": "Haben Sie schon versucht, das Problem mit einem Handtuch zu erschlagen?",  # Adams
        "your_computer_retire": "Ihr Computer hat beschlossen, in den Ruhestand zu gehen. Vielleicht überzeugen ihn ein paar Kekse?",  
        # Eigene Erfahrung + Monty Python
        "click_faster": "Klicken Sie schneller! Die Bits sind scheu.", # Eigene Erfahrung (leicht modifiziert)
        "universe_hiccup": "Das Universum hat einen kleinen Schluckauf. Einfach ignorieren.", # Eigene + Adams
        "answer_42": "42 ist die Antwort auf Ihr Problem. Was genau das Problem war, ist jetzt allerdings gelöscht...",
        "thank_you": "Danke für die Unterstützung der intergalaktischen Umgehungsstraße.\nBitte verlassen Sie Ihren Planeten.\n💣 Zerstörung beginnt in 5 Minuten! 💥" 
        #    Adams + Eigene
        },
    "en" : {
        "become_smarter": "Have you tried becoming smarter?",
        "click_harder": "Please click harder. That should help.",
        "restart_universe": "Please restart the universe and try again.",
        "problem_ignored": "We ignored your problem. Good luck!",
        "problem_moved": "Your problem has been moved to the clipboard.",
        "dau_detected": "DAU detected - sarcasm is starting...",
        "turn_off_device": "Turn off the device and think about your decisions.",
        "cant_open_dau_console": "Couldn't open DAU console. Data overflow in Wi-Fi cable.",
        "tried_with_towel": "Have you tried smacking the problem with a towel?",
        "your_computer_retire": "Your computer has decided to retire. Maybe some cookies will convince it?",
        "click_faster": "Click faster! The bits are skittish.",
        "universe_hiccup": "The universe is having a little hiccup. Just ignore it.",
        "answer_42": "42 is the answer to your problem. However, what exactly the problem was is now deleted...",
        "thank_you": "Thank you for supporting the Intergalactic Bypass.\nPlease leave your planet.\n💣 Destruction begins in 5 minutes! 💥"

        }
    }

random_quotes = {
    "de" : {
        "rebooted_universe": "Du hast das Universum neu gestartet. Glückwunsch.",
        "stroke_a_bit": "Heute schon ein Bit gestreichelt?",
        "System_error_0815": "Systemfehler 0815: Hirn nicht gefunden – bitte neu booten.",
        "overrated_reality": "Die Realität ist überbewertet.",
        "42_is_the_answer": "42 ist die Antwort. Was war nochmal die Frage?",
        "only_askers": "Nur wer fragt, bekommt auch absurde Antworten."
        },
    "en" : {
        "rebooted_universe": "You've rebooted the universe. Congratulations.",
        "stroke_a_bit": "Have you stroked a bit today?",
        "System_error_0815": "System error 0815: Brain not found – please reboot.",
        "overrated_reality": "Reality is overrated.",
        "42_is_the_answer": "42 is the answer. What was the question again?",
        "only_askers": "Only those who ask will get absurd answers."
        }
    }


exit_responses = {
    "de" : {
        "break_up": "Du willst wirklich mit mir Schluss machen?",
        "tried_alt_f4": "Schon mal Alt+F4 versucht?",
        "try_strg_f4": "Probier mal Strg+F4!",
        "you_can_do_it": "Du schaffst das, streng Deine 2 Hirnzellen an!",
        "thought_friends": "Ich dachte, wir wären Freunde...",
        "quit": "Beenden? Das wäre ja... funktional.",
        "no_must_to_press": "Nur weil es einen Button gibt, muss man ihn doch nicht drücken!",
        "come_on": "Ach, komm schon...",
        "never": "Niemals!",
        "wont_work": "So wird das nix...",
        "strg_alt_delete": "Strg+Alt+Entf hilft (fast) immer!"
        },
    "en" : {
        "break_up": "You really want to break up with me?",
        "tried_alt_f4": "Have you ever tried Alt+F4?",
        "try_strg_f4": "Try Ctrl+F4!",
        "you_can_do_it": "You can do it, use your two brain cells!",
        "thought_friends": "I thought we were friends...",
        "quit": "Quit? That would be... functional.",
        "no_must_to_press": "Just because there's a button doesn't mean you have to press it!",
        "come_on": "Oh, come on...",
        "never": "Never!",
        "wont_work": "It won't work like that...",
        "strg_alt_delete": "Ctrl+Alt+Delete (almost) always works!"
        }
    }


excuses = {
    "de" : {
        "wifi_aten": "Mein Hamster hat das WLAN gefressen.",
        "downtime": "Ich dachte, der Computer braucht auch mal Freizeit.",
        "just_ok": "Ich hab nur auf OK gedrückt!",
        "already": "Das war schon so, als ich kam.",
        "blinding": "Die Sonne blendete meine Maus.",
        "red_cable": "Ich dachte, das rote Kabel ist zur Deko.",
        "my_coffee": "Mein Kaffee hat die Tastatur gehackt.",
        "sacrifices": "Windows wollte ein Opfer – ich hab’s gebracht.",
        "feature_test": "Ich wollte das Feature 'System neu interpretieren' testen.",
        "deinstallation": "Ich hab die Realität aus Versehen deinstalliert."
    },
    "en" : {
        "wifi_aten": "My hamster ate the Wi-Fi.",
        "downtime": "I thought the computer needed some downtime.",
        "just_ok": "I just pressed OK!",
        "already": "It was like that when I arrived.",
        "blinding": "The sun was blinding my mouse.",
        "red_cable": "I thought the red cable was for decoration.",
        "my_coffee": "My coffee hacked the keyboard.",
        "sacrifices": "Windows wanted a sacrifice – I made it.",
        "feature_test": "I wanted to test the 'Reinterpret System' feature.",
        "deinstallation": "I accidentally uninstalled reality."
        }
    }
        

calming_quotes = {
    "de" : {
        "dont_panic": "Keine Panik. Es sieht nur so aus, als wäre alles kaputt.",
        "breathe": "Atmen. Tippen. Hoffen.",
        "burning": "Selbst wenn alles brennt: Es ist nur ein Feature.",
        "42": "42. Mehr musst du nicht wissen.",
        "AI": "Die KI ist auf deiner Seite... meistens.",
        "works": "Funktioniert bei mir. – Du kannst also nichts falsch gemacht haben.",
        "patience": "Geduld du haben musst, junger DAU.",
        "strong": "Stark in dir, der Fehler ist.",
        "kernel": "Das Kernel mit dir sein wird... wenn dein Handtuch du findest."
        },
    "en" : {
        "dont_panic": "Don't panic. It just looks like everything's broken.",
        "breathe": "Breathe. Type. Hope.",
        "burning": "Even if everything's on fire: It's just a feature.",
        "42": "42. That's all you need to know.",
        "AI": "The AI ​​is on your side... most of the time.",
        "works": "Works for me. – So you can't have done anything wrong.",
        "patience": "You have to be patient, young idiot.",
        "strong": "Strong in you, the mistake is.",
        "kernel": "The kernel will be with you... when you find your towel."
        }
    }

# Texte für den "Beipackzettel"-Dialog (create_sidefx_dialog)
sidefx_texts = {
    "de": {
        "lbl1": "Die Nutzung dieses Programms erfolgt auf eigene Gefahr!\n Wir übernehmen keine Haftung für vorgetäuschte/tatsächliche Hardwareschäden\nund erst recht nicht für hypochondrische/reelle Gesundheitsschäden\nwie verbrannte/kollabierte Synapsen und deren Langzeit- oder Spätfolgen.",
        "lbl2": "Nicht gemeldete oder beobachtete, aber zu erwartende,\nunterschiedlich absurde Nebenwirkungen nach Skill gruppiert:",
        "lbl3_title": "Unwissende mit Erfahrung in Mausschubsen und 2-Fingertechnik",
        "lbl4_effects": " - Stirnrunzeln mit ???\n -  Unverständnis\n -  Kopfschütteln\n -  müdes Lächeln und Augenrollen",
        "lbl5_title": "galaktische Hitchhiker",
        "lbl6_effects": " - spontane, unkontrollierte Lachanfälle/-krämpfe mit tränenden Augen\n -  schwenken des weißen Handtuchs\n -  rumkugeln auf dem Boden mit o.g. Symptomen\n -  Erstickungstod durch Lachen (eher selten)",
        "lbl7_title": "DAUs",
        "lbl8_effects": " - extreme Verwirrtheit\n -  unfassbare Ungläubigkeit\n -  Panikattacken/Angstzustände\n -  Verlust des Selbstwertgefühls\n -  angespannte Nervösitat\n -  Nervenzusammenbruch, Wutausbrüche, Gewaltexzesse gegen Computer\n -  Herzversagen nach Ermittlung des entstandenen Sachschadens",
        "lbl9_advice": "Sollte eins der o.g. Symptome bei Ihnen auftreten,\nsuchen Sie KEINESFALLS einen Arzt auf!\nAtmen Sie tief ein.\nNehmen Sie ihr Handtuch und pressen Sie es vor das Gesicht.\nZählen Sie laut aber langsam bis 42...\nDenken Sie an nichts anderes als an 42.\nJetzt können Sie wieder ausatmen und losheulen..."
        },
    "en": {
        "lbl1": "Use this program at your own risk!\nWe assume no liability for faked/actual hardware damage,\nand certainly not for hypochondriac/real health damage,\nsuch as burned/collapsed synapses and their long-term or delayed consequences.",
        "lbl2": "Unreported or observed, but expected,\nvariously absurd side effects grouped by skill:",
        "lbl3_title": "Ignorant people with experience in mouse pushing and two-finger technique",
        "lbl4_effects": " - Frowning with ???\n - Incomprehension\n - Head shaking\n - Tired smiles and eye rolling",
        "lbl5_title": "Galactic hitchhikers",
        "lbl6_effects": " - Spontaneous, uncontrolled fits of laughter/laughing with watery eyes\n - Waving the white towel\n - Rolling around on the floor with above-mentioned symptoms\n - Suffocation from laughter (rather rare)",
        "lbl7_title": "DAUs",
        "lbl8_effects": " - extreme confusion\n - unbelievable disbelief\n - panic attacks/anxiety\n - loss of self-esteem\n - tense nervousness\n - nervous breakdown, outbursts of anger, violent acts against computers\n - heart failure after determining the property damage",
        "lbl9_advice": "If you experience any of the above-mentioned symptoms,\n DO NOT seek medical attention!\nTake a deep breath.\nTake your towel and press it to your face.\nCount out loud but slowly to 42...\nDon't think about anything else but 42.\nNow you can breathe out and start crying..."
        }
    }

# Texte für den "ACHTUNG!!!"-Dialog (create_warning_dialog)
warning_dialog_texts = {
    "de": {
        "main_warning": "Diese Software darf nicht benutzt werden",
        "vogon_offices": "in vogonischen Büros",
        "pan_galactic_gargle_blaster": "unter Einfluss von pangalaktischem Donnergurgler",
        "no_towel": "wenn Sie Ihr Handtuch verloren/vergessen haben",
        "babel_fish_fired": "wenn Ihr Babelfisch gekündigt hat",
        "answer_unknown": "die Antwort auf alles unbekannt ist"
        },
    "en": {
        "main_warning": "This software is not to be used",
        "vogon_offices": "in Vogon offices",
        "pan_galactic_gargle_blaster": "under the influence of Pan Galactic Gargle Blaster",
        "no_towel": "if you have lost/forgotten your towel",
        "babel_fish_fired": "if your Babel fish has quit",
        "answer_unknown": "the answer to everything is unknown"
        }
    }

# Schritte für den Fake-Optimierungsdialog (run_fake_optimization_steps_dialog)
fake_optimization_steps = {
    "de" : {
        "partitioning": "Linux-Partition wird erstellt...",
        "downlading": "Linux-Distribution wird heruntergeladen...",
        "copying": "Wird kopiert...",
        "formatting": "Laufwerk C: wird formatiert... 😱",
        "installation": "Installation startet nach Neustart...",
        "continue": "Press any key to continue,\nor press any other to abort."       
    },
    "en" : {
        "partitioning": "Creating Linux partition...",
        "downloading": "Downloading Linux distribution...",
        "copying": "Copying...",
        "formatting": "Formatting drive C:... 😱",
        "installation": "Installation will start after reboot...",
        "continue": "Press any key to continue,\npress any other to abort."
        }
    }

menubar_texts = {
    "de": {
        "file": "Datei",
        "extras": "Extras",
        "help": "Hilfe",
        "meta": "Meta",
        },
    "en": {
        "file": "File",
        "extras": "Extras",
        "help": "Help",
        "meta": "Meta",
        }
    }

menu_item_texts = {
    "de": {
        "new_futility": "Neue Sinnlosigkeit",
        "undo_all": "Alles rückgängig machen",
        "sarcastic_exit": "Beenden?",
        "invisible_options": "Unsichtbare Optionen anzeigen",
        "do_nothing": "Nichts tun",
        "analyze_system": "System analysieren",
        "optimization": "System optimieren",
        "about": "Über DAUs forty-two",
        "help_purpose": "Was soll das alles?",
        "easter_egg": "Easter Egg finden",
        "sidefx": "Beipackzettel",
        "warning": "⚠ Wichtig! ⚠",
        },
    "en": {
        "new_futility": "New Futility",
        "undo_all": "Undo All",
        "sarcastic_exit": "Exit?",
        "invisible_options": "Show Invisible Options",
        "do_nothing": "Do Nothing",
        "analyze_system": "Analyze System",
        "optimization": "Optimize System",
        "about": "About DAUs forty-two",
        "help_purpose": "What's all this about?",
        "easter_egg": "Find Easter Egg",
        "sidefx": "Package Insert",
        "warning": "⚠ Important! ⚠",
        }
    }

welcome_texts = {
    "de": {
        "welcome": "Willkommen bei DAUs forty-two",
        "active_mode": "(DAU-Mode für Dummies aktiv)",
        },
    "en": {
        "welcome": "Welcome to DAUs forty-two",
        "active_mode": "(DAU-Mode for dumbies active)",
        }
    }

install_steps = {
    "de": {
        "towel": "Handtuch", 
        "babel_fish": "Babelfisch",
        "sub_etha": "Sub-Etha-Sender",
        "vogon_poetry": "Vogonen-Poesie-Modul",
        "improbability": "Unwahrscheinlichkeits-Drive",
        "deep_thought": "Deep Thought KI", 
        "secret_keys": "geheime Tastenkombinationen",
        "sarcasm_v2": "Sarkasmus-Modul V2"
        },
    "en": {
        "towel": "towel", 
        "babel_fish": "babel fish",
        "sub_etha": "Sub-Etha transmitter",
        "vogon_poetry": "vogon poetry module",
        "improbability": "improbability drive",
        "deep_thought": "Deep Thought AI", 
        "secret_keys": "secret key combinations",
        "sarcasm_v2": "sarcasm module V2"
        }
    }


