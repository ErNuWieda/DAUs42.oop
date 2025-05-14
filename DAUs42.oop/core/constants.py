"""
Sammlung von konstanten Textlisten für humorvolle Meldungen und Dialoge in der DAUs42-Anwendung.
Diese Listen werden verwendet, um zufällige, thematisch passende Nachrichten anzuzeigen.
"""
internet_status = [
    "Druck des Internets wurde erfolgreich gestartet.",
    "Papier reicht nicht. Versuche, WLAN nachzufüllen...",
    "Ausdruck erfolgt wunschgemäß in weißer Rhesus-B-Schrift auf transparentem Papier.",
    "Fehler 404 – Tinte nicht gefunden.",
    "Druckseite 1 von ∞ – bitte warten Sie galaktisch geduldig.",
    "Fertig... in 300.059.316 Jahren.\nSollen wir solange was spielen?"
]

dau_responses = [
    "Haben Sie schon versucht, intelligenter zu werden?",
    "Klicken Sie bitte fester. Das hilft bestimmt.",
    "Bitte starten Sie das Universum neu und versuchen Sie es erneut.",
    "Wir haben Ihr Problem ignoriert. Viel Erfolg!",
    "Ihr Problem wurde in die Rundablage verschoben.",
    "DAU erkannt – Sarkasmus wird hochgefahren...",
    "Schalten Sie das Gerät aus und denken Sie über Ihre Entscheidungen nach.",
    "Konnte DAU-Konsole nicht öffnen. Daten-Überlauf im WLAN-Kabel.",
    "Haben Sie schon versucht, das Problem mit einem Handtuch zu erschlagen?",  # Adams
    "Ihr Computer hat beschlossen, in den Ruhestand zu gehen. Vielleicht überzeugen ihn ein paar Kekse?",  
    # Eigene Erfahrung + Monty Python
    "Klicken Sie schneller! Die Bits sind scheu.", # Eigene Erfahrung (leicht modifiziert)
    "Das Universum hat einen kleinen Schluckauf. Einfach ignorieren.", # Eigene + Adams
    "42 ist die Antwort auf Ihr Problem. Was genau das Problem war, ist jetzt allerdings gelöscht...",
    "Danke für die Unterstützung der intergalaktischen Umgehungsstraße.\nBitte verlassen Sie Ihren Planeten.\n💣 Zerstörung beginnt in 5 Minuten! 💥" 
    #    Adams + Eigene
]

random_quotes = [
    "Du hast das Universum neu gestartet. Glückwunsch.",
    "Heute schon ein Bit gestreichelt?",
    "Systemfehler 0815: Hirn nicht gefunden – bitte neu booten.",
    "Die Realität ist überbewertet.",
    "42 ist die Antwort. Was war nochmal die Frage?",
    "Nur wer fragt, bekommt auch absurde Antworten."
]

exit_responses = [
    "Du willst wirklich mit mir Schluss machen?",
    "Schon mal Alt+F4 versucht?",
    "Probier mal Strg+F4!",
    "Du schaffst das, streng Deine 2 Hirnzellen an!",
    "Ich dachte, wir wären Freunde...",
    "Beenden? Das wäre ja... funktional.",
    "Nur weil es einen Button gibt, muss man ihn doch nicht drücken!",
    "Ach, komm schon...",
    "Niemals!",
    "So wird das nix...",
    "Strg+Alt+Entf hilft (fast) immer!"
]

excuses = [
    "Mein Hamster hat das WLAN gefressen.",
    "Ich dachte, der Computer braucht auch mal Freizeit.",
    "Ich hab nur auf OK gedrückt!",
    "Das war schon so, als ich kam.",
    "Die Sonne blendete meine Maus.",
    "Ich dachte, das rote Kabel ist zur Deko.",
    "Mein Kaffee hat die Tastatur gehackt.",
    "Windows wollte ein Opfer – ich hab’s gebracht.",
    "Ich wollte das Feature 'System neu interpretieren' testen.",
    "Ich hab die Realität aus Versehen deinstalliert."
]

warning_icons = [
    "⚠", "🚫", "💥", "☢", "🧨","💣",
]

calming_quotes = [
    "Keine Panik. Es sieht nur so aus, als wäre alles kaputt.",
    "Atmen. Tippen. Hoffen.",
    "Selbst wenn alles brennt: Es ist nur ein Feature.",
    "42. Mehr musst du nicht wissen.",
    "Die KI ist auf deiner Seite... meistens.",
    "Funktioniert bei mir. – Du kannst also nichts falsch gemacht haben.",
    "Geduld du haben musst, junger DAU.",
    "Stark in dir, der Fehler ist.",
    "Das Kernel mit dir sein wird... wenn dein Handtuch du findest."
]

# Texte für den "Beipackzettel"-Dialog (create_sidefx_dialog)
sidefx_texts = {
    "lbl1": "Die Nutzung dieses Programms erfolgt auf eigene Gefahr!\n Wir übernehmen keine Haftung für vorgetäuschte/tatsächliche Hardwareschäden\nund erst recht nicht für hypochondrische/reelle Gesundheitsschäden\nwie verbrannte/kollabierte Synapsen und deren Langzeit- oder Spätfolgen.",
    "lbl2": "Nicht gemeldete oder beobachtete, aber zu erwartende,\nunterschiedlich absurde Nebenwirkungen nach Skill gruppiert:",
    "lbl3_title": "Unwissende mit Erfahrung in Mausschubsen und 2-Fingertechnik",
    "lbl4_effects": "- Stirnrunzeln mit ???\n- Unverständnis\n- Kopfschütteln\n- müdes Lächeln und Augenrollen",
    "lbl5_title": "galaktische Hitchhiker",
    "lbl6_effects": "- spontane, unkontrollierte Lachanfälle/-krämpfe mit tränenden Augen\n- schwenken des weißen Handtuchs\n- rumkugeln auf dem Boden mit o.g. Symptomen\n- Erstickungstod durch Lachen (eher selten)",
    "lbl7_title": "DAUs",
    "lbl8_effects": "- extreme Verwirrtheit\n- unfassbare Ungläubigkeit\n- Panikattacken/Angstzustände\n- Verlust des Selbstwertgefühls\n- angespannte Nervösitat\n- Nervenzusammenbruch, Wutausbrüche, Gewaltexzesse gegen Computer\n- Herzversagen nach Ermittlung des entstandenen Sachschadens",
    "lbl9_advice": "Sollte eins der o.g. Symptome bei Ihnen auftreten,\nsuchen Sie KEINESFALLS einen Arzt auf!\nAtmen Sie tief ein.\nNehmen Sie ihr Handtuch und pressen Sie es vor das Gesicht.\nZählen Sie laut aber langsam bis 42...\nDenken Sie an nichts anderes als an 42.\nJetzt können Sie wieder ausatmen und losheulen..."
}

# Texte für den "ACHTUNG!!!"-Dialog (create_warning_dialog)
warning_dialog_texts = {
    "main_warning": "Diese Software darf nicht benutzt werden",
    "vogon_offices": "in vogonischen Büros",
    "pan_galactic_gargle_blaster": "unter Einfluss von pangalaktischem Donnergurgler",
    "no_towel": "wenn Sie Ihr Handtuch verloren/vergessen haben",
    "babel_fish_fired": "wenn Ihr Babelfisch gekündigt hat",
    "answer_unknown": "die Antwort auf alles unbekannt ist"
}

# Schritte für den Fake-Optimierungsdialog (run_fake_optimization_steps_dialog)
fake_optimization_steps = [
    "Linux-Partition wird erstellt...",
    "Linux-Distribution wird heruntergeladen...",
    "Wird kopiert...",
    "Laufwerk C: wird formatiert... 😱",
    "Installation startet nach Neustart...",
    "Press any key to continue,\nor press any other to abort."
]