from backend.universal.enums import War_Bond, Penetration, Style

## Primary / Secondary / Throwable / Strat / Armor Passive / Booster | Top Layer
## 01        02          03          04      05              06

## Subclass 1 / Subclass 2 / Subclass 3 / Subclass 4 / Subclass 5 | Second Layer
## 01           02           03           04           05

## ID:Sequential | Third Layer

##Together: Top Layer | Second Layer | Third Layer
##Example:  01          01             01       010101

primary = {
    "Assault Rifle": [ 
        ("AR-23 Liberator", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.BASE,                  
            "ID": "010101", 
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("AR-23C Liberator Concussive", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.STEELED_VETERANS,      
            "ID": "010102",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("AR-23P Liberator Penetrator", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,   
            "ID": "010103",
            "Style": [[Style.DEFAULT, Style.SPECOPS]]
            }),  
        ("StA-52 Assault Rifle", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.KILLZONE_CROSSOVER,    
            "ID": "010104",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("AR-23A Liberator Carbine", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.VIPER_COMMANDOS,       
            "ID": "010105",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("AR-61 Tenderizer", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.POLAR_PATRIOTS,        
            "ID": "010106",
            "Style": Style.SPECOPS
            }),  
        ("BR-14 Adjudicator", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "010107",
            "Style": Style.SPECOPS
            }),  
        ("AR-32 Pacifier", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.FORCE_OF_LAW,          
            "ID": "010108",
            "Style": Style.DEFAULT
            }),
        ("AR-2 Coyote", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DUST_DEVILS,           
            "ID": "010109",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),
        ("MA5C Assault Rifle", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.ODST,                  
            "ID": "010110",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),
    ],
    "Marksman Rifle": [
        ("R-2124 Constitution", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BASE, 
            "ID": "010201",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("R-63 Diligence", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "010202",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("R-63CS Diligence Counter Sniper", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "010203",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("R-2 Amendment", { 
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.MASTERS_OF_CEREMONY, 
            "ID": "010204",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("R-6 Deadeye", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BORDERLINE_JUSTICE, 
            "ID": "010205",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  

    ],
    "Sniper Rifle": [
        ("PLAS-39 Accelerator Rifle", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BASE, 
            "ID": "010301",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]})  
    ],
    "Submachine Gun": [
        ("SMG-32 Reprimand", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.TRUTH_ENFORCERS,       
            "ID": "010401",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("SMG-37 Defender", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,   
            "ID": "010402",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }), 
        ("MP-98 Knight", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.SUPER_CITIZEN_EDITION, 
            "ID": "010403",
            "Style": [Style.SPECOPS]
            }),  
        ("StA-11 SMG", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.KILLZONE_CROSSOVER,    
            "ID": "010404",
            "Style": [Style.DEFAULT, Style.SPECOPS]}),  
        ("SMG-72 Pummeler", 
         {"Penetration": Penetration.LIGHT,  
          "Warbond": War_Bond.POLAR_PATRIOTS,        
          "ID": "010405",
          "Style": [Style.DEFAULT]
          }),  
        ("M7S SMG", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.ODST,                  
            "ID": "010406",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]})
    ],
    "Shotgun": [
        ("SG-20 Halt", {
            "Penetration": [Penetration.LIGHT, Penetration.MEDIUM], 
            "Warbond": War_Bond.TRUTH_ENFORCERS, 
            "ID": "010501",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
        ("SG-225 Breaker", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,                  
            "ID": "010502",
            "Style": [Style.DEFAULT]
            }),  
        ("SG-225SP Breaker Spray & Pray", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,                   
            "ID": "010503",
            "Style": [Style.DEFAULT, Style.SPECOPS]}),  
        ("SG-225IE Breaker Incendiary", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.STEELED_VETERANS,                      
            "ID": "010504",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),    
        ("SG-451 Cookout", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.FREEDOMS_FLAME,                        
            "ID": "010505",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),  
        ("SG-8 Punisher", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,                   
            "ID": "010506",
            "Style": [Style.DEFAULT]
            }),  
        ("SG-8S Slugger", {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,                  
            "ID": "010507",
            "Style": [Style.SPECOPS]}),  
        ("M90A Shotgun", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.ODST,                                  
            "ID": "010508",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]}),  
    ],
    "Energy Based": [
        ("LAS-16 Sickle", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "010601",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("LAS-17 Double-Edge Sickle", {
            "Penetration": Penetration.HEAVY,  
            "Warbond": War_Bond.SERVANTS_OF_FREEDOM, 
            "ID": "010602",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]}),  
        ("LAS-5 Scythe", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "010603",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("SG-8P Punisher Plasma", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "010604",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]}),  
        ("ARC-12 Blitzer", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "010605",
            "Style": [Style.DEFAULT, Style.SPECOPS]}), 
        ("PLAS-1 Scorcher", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "010606",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("PLAS-101 Purifier", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.POLAR_PATRIOTS, 
            "ID": "010607", 
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            })  
    ],
    "Special": [
        ("FLAM-66 Torcher", {
            "Penetration": Penetration.HEAVY,  
            "Warbond": War_Bond.FREEDOMS_FLAME, 
            "ID": "010701",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),  
        ("JAR-5 Dominator", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.STEELED_VETERANS, 
            "ID": "010702",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),  
        ("VG-70 Variable", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.CONTROL_GROUP, 
            "ID": "010703",
            "Style": [Style.DEFAULT]})
    ],
    "Explosive": [
        ("CB-9 Exploding Crossbow", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "010801",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("R-36 Eruptor", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "010802",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            })  
    ]
}

secondary = {
    "Pistol": [
        ("P-2 Peacemaker", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.BASE, 
            "ID": "020101",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("P-19 Redeemer", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "020102",
            "Style": [Style.DEFAULT]
            }),  
        ("P-113 Verdict", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.POLAR_PATRIOTS, 
            "ID": "020103",
            "Style": [Style.SPECOPS]}),  
        ("P-4 Senator", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.STEELED_VETERANS, 
            "ID": "020104",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("P-92 Warrant", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.FORCE_OF_LAW, 
            "ID": "020105",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("M6C/SOCOM Pistol", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.ODST, 
            "ID": "020106",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            })

    ],
    "Melee": [
        ("CQC-19 Stun Lance", {
            "Penetration": Penetration.MEDIUM,
              "Warbond": War_Bond.URBAN_LEGENDS, 
              "ID": "020201",
              "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
              }), 
        ("CQC-30 Stun Baton", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.SUPER_STORE, 
            "ID": "020202",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("CQC-5 Combat Hatchet", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.SUPER_STORE, 
            "ID": "020203",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]}), 
        ("CQC-2 Saber", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.MASTERS_OF_CEREMONY, 
            "ID": "020204",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),
        ("CQC-42 Machete", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.SUPER_STORE, 
            "ID": "020205",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            })
    ],
    "Special": [
        ("P-11 Stim Pistol", {
            "Penetration": None, 
            "Warbond": War_Bond.CHEMICAL_AGENTS, 
            "ID": "020301",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("SG-22 Bushwhacker", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.VIPER_COMMANDOS, 
            "ID": "020302",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("P-72 Crisper", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.FREEDOMS_FLAME, 
            "ID": "020303",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]}),  
        ("GP-31 Grenade Pistol", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "020304",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]}),  
        ("LAS-7 Dagger", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "020305",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("GP-31 Ultimatum", {
            "Penetration": ["Anti-Tank IV", "Anti-Tank II"], 
            "Warbond": War_Bond.SERVANTS_OF_FREEDOM, 
            "ID": "020306",  
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),
        ("PLAS-15 Loyalist", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.TRUTH_ENFORCERS, 
            "ID": "020307",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],            
            }),  
        ("LAS-58 Talon", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BORDERLINE_JUSTICE, 
            "ID": "020308",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            })
    ]
}

throwable = {
    "Standard": [
        ("G-6 Frag", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BASE, 
            "ID": "030101",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            }),  
        ("G-12 High Explosive", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.BASE, 
            "ID": "030102",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
            }),  
        ("G-10 Incendiary", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.STEELED_VETERANS, 
            "ID": "030103",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            }),  
        ("TED-63 Dynamite", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.BORDERLINE_JUSTICE, 
            "ID": "030104",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
            }),
        ("G-7 Pineapple", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DUST_DEVILS, 
            "ID": "030105",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            })
    ],
    "Special": [
        ("G-16 Impact", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "030201",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
            }),  
        ("G-13 Incendiary Impact", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.POLAR_PATRIOTS, 
            "ID": "030202",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            }),  
        ("G-23 Stun", {
            "Penetration": None, 
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "030203",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
        ("G-4 Gas", {
            "Penetration": Penetration.ANTI_TANK_2, 
            "Warbond": War_Bond.CHEMICAL_AGENTS, 
            "ID": "030203",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
        ("G-50 Seeker", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.SERVANTS_OF_FREEDOM, 
            "ID": "030204",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
        ("G-3 Smoke", {
            "Penetration": "unarmored I", 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "030205",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
        ("G-123 Thermite", {
            "Penetration": "tank III", 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "030206",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],}),  
        ("K-2 Throwing Knife", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.VIPER_COMMANDOS, 
            "ID": "030207",
            "Style": [Style.DEFAULT, Style.SPECOPS],}),  
        ("G-142 Pyrotech", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.MASTERS_OF_CEREMONY, 
            "ID": "030208",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],}),
        ("G-109 Urchin", {
            "Penetration": Penetration.TANK_2, 
            "Warbond": War_Bond.FORCE_OF_LAW, 
            "ID": "030209",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),
        ("G-31 Arc", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.CONTROL_GROUP, 
            "ID": "030210",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            })
    ]
}

Stratagems = {
    "Blue": {
        "MG-43 Machine Gun": {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040101",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "APW-1 Anti-Materiel Rifle": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040102",
            "Style": [Style.SPECOPS],
        },
        "M-105 Stalwart": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040103",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "EAT-17 Expendable Anti-Tank": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040103",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS],
        },
        "GR-8 Recoilless Rifle": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040104",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "FLAM-40 Flamethrower": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040105",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
        },
        "AC-8 Autocannon": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040106",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
        },
        "MG-206 Heavy Machine Gun": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040107",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "RL-77 Airburst Rocket Launcher": {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040108",
            "Style": [Style.EXPLOSIVE],
        },
        "MLS-4X Commando": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040109",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS],
        },
        "RS-422 Railgun": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040109",
            "Style": [Style.SPECOPS, Style.DEFAULT],
        },
        "FAF-14 Spear": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040110",
            "Style": [Style.SPECOPS, Style.DEFAULT],
        },
        "StA-X3 W.A.S.P. Launcher": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040111",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
        },
        "LIFT-850 Jump Pack": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040112",
            "Style": [Style.SPECOPS, Style.DEFAULT],
        },
        "M-102 Fast Reconnaissance Vehicle": {
            "Penetration": None,
            "Warbond": War_Bond.URBAN_LEGENDS,
            "pack": False,
            "ID": "040113",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "B-1 Supply Pack": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040114",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.DEFAULT],
        },
        "GL-21 Grenade Launcher": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040115",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "LAS-98 Laser Cannon": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040116",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "AX/LAS-5 'Guard Dog' Rover": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040117",
            "Style": [Style.DEFAULT],
        },
        "SH-20 Ballistic Shield Backpack": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040118",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "ARC-3 Arc Thrower": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040119",
            "Style": [Style.SPECOPS, Style.DEFAULT],
        },
        "LAS-99 Quasar Cannon": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040120",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
        },
        "SH-32 Shield Generator Pack": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040121",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "AX/AR-23 'Guard Dog'": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040122",
            "Style": [Style.DEFAULT],
        },
        "EXO-45 Patriot Exosuit": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040123",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
        },
        "EXO-49 Emancipator Exosuit": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040124",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
        },
        "TX-41 Sterilizer": {
            "Penetration": None,
            "Warbond": War_Bond.CHEMICAL_AGENTS,
            "pack": False,
            "ID": "040125",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "AX/TX-13 'Guard Dog' Dog Breath": {
            "Penetration": None,
            "Warbond": War_Bond.CHEMICAL_AGENTS,
            "pack": True,
            "ID": "040126",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "SH-51 Directional Shield": {
            "Penetration": None,
            "Warbond": War_Bond.URBAN_LEGENDS,
            "pack": True,
            "ID": "040127",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "B-100 Portable Hellbomb": {
            "Penetration": Penetration.ANTI_TANK_4,
            "Warbond": War_Bond.SERVANTS_OF_FREEDOM,
            "pack": True,
            "ID": "040128",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
        },
        "EAT-700 Expendable Napalm": {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.DUST_DEVILS,
            "pack": False,
            "ID": "040129",
            "Style": [Style.EXPLOSIVE],
        },
        "MS-11 Solo Silo": {
            "Penetration": [Penetration.ANTI_TANK_3, Penetration.ANTI_TANK_5],
            "Warbond": War_Bond.DUST_DEVILS,
            "pack": False,
            "ID": "040130",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
        },
        "S-11 Speargun": {
            "Penetration": [Penetration.ANTI_TANK_1, Penetration.ANTI_TANK_2, Penetration.UNARMORED_1],
            "Warbond": War_Bond.DUST_DEVILS,
            "pack": False,
            "ID": "040131",
            "Style": [Style.SPECOPS, Style.DEFAULT],
        },
        "LIFT-182 Warp Pack": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.CONTROL_GROUP,
            "pack": True,
            "ID": "040132",
            "Style": [Style.SPECOPS, Style.DEFAULT],
        },
        "PLAS-45 Epoch": {
            "Penetration": [Penetration.HEAVY, Penetration.ANTI_TANK_1],
            "Warbond": War_Bond.CONTROL_GROUP,
            "pack": False,
            "ID": "040133",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
        },
        "AX/ARC-3 'Guard Dog' K-9": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.ANTI_TANK_3],
            "Warbond": War_Bond.FORCE_OF_LAW,
            "pack": True,
            "ID": "040134",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "GL-52 De-Escalator": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.HEAVY, Penetration.ANTI_TANK_2],
            "Warbond": War_Bond.FORCE_OF_LAW,
            "pack": False,
            "ID": "040135",
            "Style": [Style.SPECOPS, Style.DEFAULT],
        },
        "CQC-1 One True Flag": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.MEDIUM],
            "Warbond": War_Bond.MASTERS_OF_CEREMONY,
            "pack": False,
            "ID": "040136",
            "Style": [Style.SPECOPS, Style.DEFAULT, Style.EXPLOSIVE],
        },
        "LIFT-860 Hover Pack": {
            "Penetration": None,
            "Warbond": War_Bond.BORDERLINE_JUSTICE,
            "pack": True,
            "ID": "040137",
            "Style": [Style.SPECOPS, Style.DEFAULT, Style.EXPLOSIVE],
        },
    },

    "Red": {
        "Orbital Gatling Barrage": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 70,
            "ID": "040201",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Orbital Airburst Strike": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "cooldown": 100,
            "ID": "040202",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Orbital 120mm HE Barrage": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "cooldown": 180,
            "ID": "040203",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Orbital 380mm HE Barrage": {
            "Penetration": "Anti-Tank IV",
            "Warbond": War_Bond.BASE,
            "cooldown": 240,
            "ID": "040204",
            "Style": [Style.EXPLOSIVE],
        },
        "Orbital Walking Barrage": {
            "Penetration": "Anti-Tank IV",
            "Warbond": War_Bond.BASE,
            "cooldown": 240,
            "ID": "040205",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Orbital Laser": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "cooldown": 300,
            "ID": "040206",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "Orbital Napalm Barrage": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 240,
            "ID": "040207",
            "Style": [Style.EXPLOSIVE],
        },
        "Orbital Railcannon Strike": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "cooldown": 210,
            "ID": "040208",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "Eagle Strafing Run": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040209",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "Eagle Airstrike": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040210",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Eagle Cluster Bomb": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040211",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Eagle Napalm Airstrike": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040212",
            "Style": [Style.EXPLOSIVE],
        },
        "Eagle Smoke Strike": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040213",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "Eagle 110mm Rocket Pods": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040214",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
        },
        "Eagle 500kg Bomb": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040215",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT, Style.SPECOPS],
        },
        "Orbital Precision Strike": {
            "Penetration": "Anti-Tank IV",
            "Warbond": War_Bond.BASE,
            "cooldown": 90,
            "ID": "040216",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS],
        },
        "Orbital Gas Strike": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "cooldown": 75,
            "ID": "040217",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
        },
        "Orbital EMS Strike": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "cooldown": 75,
            "ID": "040218",
            "Style": [Style.SPECOPS, Style.DEFAULT],
        },
        "Orbital Smoke Strike": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "cooldown": 100,
            "ID": "040219",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
    },

    "Green": {
        "E/MG-101 HMG Emplacement": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "cooldown": 180,
            "ID": "040301",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "FX-12 Shield Generator Relay": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "cooldown": 90,
            "ID": "040302",
            "Style": [Style.DEFAULT],
        },
        "A/ARC-3 Tesla Tower": {
            "Penetration": "Unarmored II",
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040303",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
        },
        "MD-6 Anti-Personnel Minefield": {
            "Penetration": "Unarmored II",
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040304",
            "Style": [Style.EXPLOSIVE],
        },
        "MD-I4 Incendiary Mines": {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040305",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "MD-17 Anti-Tank Mines": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040306",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "MD-8 Gas Mines": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040307",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "A/MG-43 Machine Gun Sentry": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "cooldown": 90,
            "ID": "040308",
            "Style": [Style.DEFAULT],
        },
        "A/G-16 Gatling Sentry": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "cooldown": 150,
            "ID": "040309",
            "Style": [Style.DEFAULT],
        },
        "A/M-12 Mortar Sentry": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "cooldown": 180,
            "ID": "040310",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/AC-8 Autocannon Sentry": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 150,
            "ID": "040311",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/MLS-4X Rocket Sentry": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 150,
            "ID": "040312",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/M-23 EMS Mortar Sentry": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 180,
            "ID": "040313",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "E/AT-12 Anti-Tank Emplacement": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.URBAN_LEGENDS,
            "cooldown": 180,
            "ID": "040314",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/FLAM-40 Flame Sentry": {
            "Penetration": [Penetration.MEDIUM, Penetration.HEAVY],
            "Warbond": War_Bond.URBAN_LEGENDS,
            "cooldown": 150,
            "ID": "040315",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/LAS-98 Laser Sentry": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.HEAVY],
            "Warbond": War_Bond.CONTROL_GROUP,
            "cooldown": 150,
            "ID": "040316",
            "Style": [Style.DEFAULT],
        },
        "E/GL-21 Grenadier Battlement": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.MEDIUM],
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040317",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
        },
    },
}

Armor_Passive = [
    {"Acclimated": {
        "Warbond": War_Bond.KILLZONE_CROSSOVER, 
        "ID": "050101",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }},            
    {"Advance Filtration": {
        "Warbond": War_Bond.CHEMICAL_AGENTS, 
        "ID": "050102",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]
        }},          
    {"Extra Padding": {
        "Warbond": War_Bond.SUPER_STORE, 
        "ID": "050103",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]
        }},                    
    {"Engineering Kit": {
        "Warbond": [War_Bond.SUPER_STORE, War_Bond.DEMOCRATIC_DETONATION], 
        "ID": "050104",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
        }}, 
    {"Med-Kit": {
        "Warbond": War_Bond.SUPER_STORE, 
        "ID": "050105",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},                          
    {"Scout": {
        "Warbond": [War_Bond.POLAR_PATRIOTS, War_Bond.HELLDIVERS_MOBILIZE], 
        "ID": "050106",
        "Tag": [Style.SPECOPS]}},  
    {"Electrical Conduit": {
        "Warbond": War_Bond.CUTTING_EDGE, 
        "ID": "050107",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},             
    {"Fortified": {
        "Warbond": War_Bond.SUPER_STORE,
          "ID": "050108",
          "Tag": [Style.EXPLOSIVE]}},                        
    {"Inflammable": {
        "Warbond": War_Bond.FREEDOMS_FLAME, 
        "ID": "050109",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]}},                 
    {"Integrated Explosives": {
        "Warbond": [War_Bond.SUPER_STORE, War_Bond.SERVANTS_OF_FREEDOM], 
        "ID": "050110",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},  
    {"Peak Physique": {
        "Warbond": War_Bond.VIPER_COMMANDOS, 
        "ID": "050111",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},               
    {"Servo-Assisted": {
        "Warbond": War_Bond.SUPER_STORE, 
        "ID": "050112",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},                   
    {"Siege-Ready": {
        "Warbond": War_Bond.URBAN_LEGENDS, 
        "ID": "050113",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},                   
    {"Unflinching": {
        "Warbond": War_Bond.TRUTH_ENFORCERS, 
        "ID": "050114",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},                  
    {"Desert Stormer": {
        "Warbond": War_Bond.DUST_DEVILS, 
        "ID": "050115",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},
    {"Feet First": {
        "Warbond": War_Bond.ODST, 
        "ID": "050116",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},
    {"Adreno-Defibrillator": {
        "Warbond": War_Bond.CONTROL_GROUP, 
        "ID": "050117",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},
    {"Ballistic Padding": {
        "Warbond": War_Bond.FORCE_OF_LAW, 
        "ID": "050118",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},
    {"Reinforced Epaulettes": {
        "Warbond": War_Bond.MASTERS_OF_CEREMONY,
          "ID": "050119",
          "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},
    {"Gunslinger": {
        "Warbond": War_Bond.BORDERLINE_JUSTICE, 
        "ID": "050120",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},
    {"Integrated Explosives": {
        "Warbond": War_Bond.SERVANTS_OF_FREEDOM, 
        "ID": "050121",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }},
]

Booster = [
    {"Hellpod Space Optimization": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060101",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
        }},  
    {"Vitality Enhancement": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060102",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},       
    {"UAV Recon Booster": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060103",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},           
    {"Stamina Enhancement": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060104",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},         
    { "Muscle Enhancement" : {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060105",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},        
    {"Increased Reinforcement Budget": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060106",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }}, 
    {"Flexible Reinforcement Budget": {
        "Warbond": War_Bond.STEELED_VETERANS, 
        "ID": "060107",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }},  
    {"Localization Confusion": {
        "Warbond": War_Bond.CUTTING_EDGE, 
        "ID": "060108",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},             
    {"Expert Extraction Pilot": {
        "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
        "ID": "060109",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},   
    {"Motivational Shocks": {
        "Warbond": War_Bond.POLAR_PATRIOTS, 
        "ID": "060110",
        "Tag": [Style.DEFAULT, Style.SPECOPS]
        }},              
    {"Experimental Infusion": {
        "Warbond": War_Bond.VIPER_COMMANDOS, 
        "ID": "060111",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]
        }},          
    {"Firebomb Hellpods": {
        "Warbond": War_Bond.FREEDOMS_FLAME, 
        "ID": "060112",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }},               
    {"Dead Sprint": {
        "Warbond": War_Bond.TRUTH_ENFORCERS, 
        "ID": "060113",
        "Tag": [Style.SPECOPS]}},                     
    {"Armed Resupply Pods": {
        "Warbond": War_Bond.URBAN_LEGENDS, 
        "ID": "060114",
        "Tag": [Style.DEFAULT,Style.SPECOPS]}},
    {"Sample Extricator": {
        "Warbond": War_Bond.BORDERLINE_JUSTICE, 
        "ID": "060115",
        "Tag": [Style.DEFAULT]
        }},
    {"Sample Scanner": {
        "Warbond": War_Bond.MASTERS_OF_CEREMONY, 
        "ID": "060116",
        "Tag": [Style.SPECOPS]}},
    {"Stun Pods": {
        "Warbond": War_Bond.FORCE_OF_LAW, 
        "ID": "060117",
        "Tag": [Style.SPECOPS]}},

]
