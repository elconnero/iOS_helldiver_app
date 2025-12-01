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
            "image_url": "010101.png", 
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("AR-23C Liberator Concussive", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.STEELED_VETERANS,      
            "ID": "010102",
            "image_url": "010102.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("AR-23P Liberator Penetrator", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,   
            "ID": "010103",
            "image_url": "010103.png",
            "Style": [[Style.DEFAULT, Style.SPECOPS]]
            }),  
        ("StA-52 Assault Rifle", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.KILLZONE_CROSSOVER,    
            "ID": "010104",
            "image_url": "010104.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("AR-23A Liberator Carbine", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.VIPER_COMMANDOS,       
            "ID": "010105",
            "image_url": "010105.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("AR-61 Tenderizer", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.POLAR_PATRIOTS,        
            "ID": "010106",
            "image_url": "010106.png",
            "Style": Style.SPECOPS
            }),  
        ("BR-14 Adjudicator", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "010107",
            "image_url": "010107.png",
            "Style": Style.SPECOPS
            }),  
        ("AR-32 Pacifier", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.FORCE_OF_LAW,          
            "ID": "010108",         
            "image_url": "010108.png",
            "Style": Style.DEFAULT
            }),
        ("AR-2 Coyote", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DUST_DEVILS,           
            "ID": "010109",    
            "image_url": "010109.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),
        ("MA5C Assault Rifle", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.ODST,                  
            "ID": "010110",
            "image_url": "010110.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),
    ],
    "Marksman Rifle": [
        ("R-2124 Constitution", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BASE, 
            "ID": "010201",
            "image_url": "010201.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("R-63 Diligence", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "010202",
            "image_url": "010202.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("R-63CS Diligence Counter Sniper", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "010203",
            "image_url": "010203.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("R-2 Amendment", { 
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.MASTERS_OF_CEREMONY, 
            "ID": "010204",
            "image_url": "010204.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("R-6 Deadeye", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BORDERLINE_JUSTICE, 
            "ID": "010205",
            "image_url": "010205.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  

    ],
    "Sniper Rifle": [
        ("PLAS-39 Accelerator Rifle", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BASE, 
            "ID": "010301",
            "image_url": "010301.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]})  
    ],
    "Submachine Gun": [
        ("SMG-32 Reprimand", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.TRUTH_ENFORCERS,       
            "ID": "010401",
            "image_url": "010401.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("SMG-37 Defender", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,   
            "ID": "010402",
            "image_url": "010402.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }), 
        ("MP-98 Knight", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.SUPER_CITIZEN_EDITION, 
            "ID": "010403",
            "image_url": "010403.png",
            "Style": [Style.SPECOPS]
            }),  
        ("StA-11 SMG", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.KILLZONE_CROSSOVER,    
            "ID": "010404",
            "image_url": "010404.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]}),  
        ("SMG-72 Pummeler", 
         {"Penetration": Penetration.LIGHT,  
          "Warbond": War_Bond.POLAR_PATRIOTS,        
          "ID": "010405",
          "image_url": "010405.png",
          "Style": [Style.DEFAULT]
          }),  
        ("M7S SMG", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.ODST,                  
            "ID": "010406",
            "image_url": "010406.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]})
    ],
    "Shotgun": [
        ("SG-20 Halt", {
            "Penetration": [Penetration.LIGHT, Penetration.MEDIUM], 
            "Warbond": War_Bond.TRUTH_ENFORCERS, 
            "ID": "010501",
            "image_url": "010501.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
        ("SG-225 Breaker", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,                  
            "ID": "010502",
            "image_url": "010502.png",
            "Style": [Style.DEFAULT]
            }),  
        ("SG-225SP Breaker Spray & Pray", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,                   
            "ID": "010503",                 
            "image_url": "010503.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]}),  
        ("SG-225IE Breaker Incendiary", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.STEELED_VETERANS,                      
            "ID": "010504",            
            "image_url": "010504.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),    
        ("SG-451 Cookout", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.FREEDOMS_FLAME,                        
            "ID": "010505",                       
            "image_url": "010505.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),  
        ("SG-8 Punisher", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,                   
            "ID": "010506",                 
            "image_url": "010506.png",
            "Style": [Style.DEFAULT]
            }),  
        ("SG-8S Slugger", {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE,                  
            "ID": "010507",
            "image_url": "010507.png",
            "Style": [Style.SPECOPS]}),  
        ("M90A Shotgun", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.ODST,                                  
            "ID": "010508",                               
            "image_url": "010508.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]}),  
    ],
    "Energy Based": [
        ("LAS-16 Sickle", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "010601",
            "image_url": "010601.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("LAS-17 Double-Edge Sickle", {
            "Penetration": Penetration.HEAVY,  
            "Warbond": War_Bond.SERVANTS_OF_FREEDOM, 
            "ID": "010602",
            "image_url": "010602.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]}),  
        ("LAS-5 Scythe", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "010603",
            "image_url": "010603.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("SG-8P Punisher Plasma", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "010604",
            "image_url": "010604.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]}),  
        ("ARC-12 Blitzer", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "010605",
            "image_url": "010605.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]}), 
        ("PLAS-1 Scorcher", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "010606",
            "image_url": "010606.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("PLAS-101 Purifier", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.POLAR_PATRIOTS, 
            "ID": "010607",
            "image_url": "010607.png", 
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            })  
    ],
    "Special": [
        ("FLAM-66 Torcher", {
            "Penetration": Penetration.HEAVY,  
            "Warbond": War_Bond.FREEDOMS_FLAME, 
            "ID": "010701",
            "image_url": "010701.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),  
        ("JAR-5 Dominator", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.STEELED_VETERANS, 
            "ID": "010702",
            "image_url": "010702.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),  
        ("VG-70 Variable", {
            "Penetration": Penetration.LIGHT,  
            "Warbond": War_Bond.CONTROL_GROUP, 
            "ID": "010703",
            "image_url": "010703.png",
            "Style": [Style.DEFAULT]})
    ],
    "Explosive": [
        ("CB-9 Exploding Crossbow", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "010801",
            "image_url": "010801.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),  
        ("R-36 Eruptor", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "010802",
            "image_url": "010802.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            })  
    ]
}

secondary = {
    "Pistol": [
        ("P-2 Peacemaker", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.BASE, 
            "ID": "020101",
            "image_url": "020101.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("P-19 Redeemer", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "020102",
            "image_url": "020102.png",
            "Style": [Style.DEFAULT]
            }),  
        ("P-113 Verdict", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.POLAR_PATRIOTS, 
            "ID": "020103",
            "image_url": "020103.png",
            "Style": [Style.SPECOPS]}),  
        ("P-4 Senator", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.STEELED_VETERANS, 
            "ID": "020104",
            "image_url": "020104.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("P-92 Warrant", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.FORCE_OF_LAW, 
            "ID": "020105",
            "image_url": "020105.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("M6C/SOCOM Pistol", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.ODST, 
            "ID": "020106",
            "image_url": "020106.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            })

    ],
    "Melee": [
        ("CQC-19 Stun Lance", {
            "Penetration": Penetration.MEDIUM,
              "Warbond": War_Bond.URBAN_LEGENDS, 
              "ID": "020201",
 
              "image_url": "020201.png",
              "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
              }), 
        ("CQC-30 Stun Baton", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.SUPER_STORE, 
            "ID": "020202",
            "image_url": "020202.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("CQC-5 Combat Hatchet", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.SUPER_STORE, 
            "ID": "020203",
            "image_url": "020203.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]}), 
        ("CQC-2 Saber", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.MASTERS_OF_CEREMONY, 
            "ID": "020204",
            "image_url": "020204.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),
        ("CQC-42 Machete", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.SUPER_STORE, 
            "ID": "020205",
            "image_url": "020205.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            })
    ],
    "Special": [
        ("P-11 Stim Pistol", {
            "Penetration": None, 
            "Warbond": War_Bond.CHEMICAL_AGENTS, 
            "ID": "020301",
            "image_url": "020301.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.EXPLOSIVE]
            }),  
        ("SG-22 Bushwhacker", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.VIPER_COMMANDOS, 
            "ID": "020302",
            "image_url": "020302.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("P-72 Crisper", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.FREEDOMS_FLAME, 
            "ID": "020303",
            "image_url": "020303.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]}),  
        ("GP-31 Grenade Pistol", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "020304",
            "image_url": "020304.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]}),  
        ("LAS-7 Dagger", {
            "Penetration": Penetration.LIGHT, 
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "020305",
            "image_url": "020305.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            }),  
        ("GP-31 Ultimatum", {
            "Penetration": ["Anti-Tank IV", "Anti-Tank II"], 
            "Warbond": War_Bond.SERVANTS_OF_FREEDOM, 
            "ID": "020306",
            "image_url": "020306.png",  
            "Style": [Style.DEFAULT, Style.EXPLOSIVE]
            }),
        ("PLAS-15 Loyalist", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.TRUTH_ENFORCERS, 
            "ID": "020307",
            "image_url": "020307.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],            
            }),  
        ("LAS-58 Talon", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BORDERLINE_JUSTICE, 
            "ID": "020308",
            "image_url": "020308.png",
            "Style": [Style.DEFAULT, Style.SPECOPS]
            })
    ]
}

throwable = { #Total: 15
    "Standard": [ # Standard Total: 5
        ("G-6 Frag", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.BASE, 
            "ID": "030101",
            "image_url": "030101.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            }),  
        ("G-12 High Explosive", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.BASE, 
            "ID": "030102",
            "image_url": "030102.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
            }),  
        ("G-10 Incendiary", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.STEELED_VETERANS, 
            "ID": "030103",
            "image_url": "030103.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            }),  
        ("TED-63 Dynamite", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.BORDERLINE_JUSTICE, 
            "ID": "030104",
            "image_url": "030104.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
            }),
        ("G-7 Pineapple", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.DUST_DEVILS, 
            "ID": "030105",
            "image_url": "030105.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            })
    ],
    "Special": [ #Total 10
        ("G-16 Impact", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "030201",
            "image_url": "030201.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
            }),  
        ("G-13 Incendiary Impact", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.POLAR_PATRIOTS, 
            "ID": "030202",
            "image_url": "030202.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            }),  
        ("G-23 Stun", {
            "Penetration": None, 
            "Warbond": War_Bond.CUTTING_EDGE, 
            "ID": "030203",
            "image_url": "030203.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
        ("G-50 Seeker", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.SERVANTS_OF_FREEDOM, 
            "ID": "030204",
            "image_url": "030204.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
        ("G-3 Smoke", {
            "Penetration": "unarmored I", 
            "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
            "ID": "030205",
            "image_url": "030205.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
        ("G-123 Thermite", {
            "Penetration": "tank III", 
            "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
            "ID": "030206",
            "image_url": "030206.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],}),  
        ("K-2 Throwing Knife", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.VIPER_COMMANDOS, 
            "ID": "030207",
            "image_url": "030207.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],}),  
        ("G-142 Pyrotech", {
            "Penetration": Penetration.MEDIUM, 
            "Warbond": War_Bond.MASTERS_OF_CEREMONY, 
            "ID": "030208",
            "image_url": "030208.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],}),
        ("G-109 Urchin", {
            "Penetration": Penetration.TANK_2, 
            "Warbond": War_Bond.FORCE_OF_LAW, 
            "ID": "030209",
            "image_url": "030209.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),
        ("G-31 Arc", {
            "Penetration": Penetration.HEAVY, 
            "Warbond": War_Bond.CONTROL_GROUP, 
            "ID": "030210",
            "image_url": "030210.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),
        ("G-4 Gas", {
            "Penetration": Penetration.ANTI_TANK_2, 
            "Warbond": War_Bond.CHEMICAL_AGENTS, 
            "ID": "030211",
            "image_url": "030211.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            }),  
    ]
}

Stratagems = {
    "Blue": {
        "MG-43 Machine Gun": {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040101",
            "image_url": "040101.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            "Support": True,
        },
        "APW-1 Anti-Materiel Rifle": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040102",
            "image_url": "040102.png",
            "Style": [Style.SPECOPS],
            "Support": True,
        },
        "M-105 Stalwart": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040103",
            "image_url": "040103.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            "Support": True,
        },
        "GR-8 Recoilless Rifle": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040104",
            "image_url": "040104.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
            "Support": True,
        },
        "FLAM-40 Flamethrower": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040105",
            "image_url": "040105.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            "Support": True,
        },
        "AC-8 Autocannon": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040106",
            "image_url": "040106.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            "Support": True,
        },
        "MG-206 Heavy Machine Gun": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040107",
            "image_url": "040107.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            "Support": True,
        },
        "RL-77 Airburst Rocket Launcher": {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040108",
            "image_url": "040108.png",
            "Style": [Style.EXPLOSIVE],
            "Support": True,
        },
        "MLS-4X Commando": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040109",
            "image_url": "040109.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS],
            "Support": True,
        },
        "RS-422 Railgun": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040109",
            "image_url": "040109.png",
            "Style": [Style.SPECOPS, Style.DEFAULT],
            "Support": True,
        },
        "FAF-14 Spear": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040110",
            "image_url": "040110.png",
            "Style": [Style.SPECOPS, Style.DEFAULT],
            "Support": True,
        },
        "StA-X3 W.A.S.P. Launcher": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040111",
            "image_url": "040111.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
            "Support": True,
        },
        "LIFT-850 Jump Pack": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040112",
            "image_url": "040112.png",
            "Style": [Style.SPECOPS, Style.DEFAULT],
            "Support": False,
        },
        "M-102 Fast Reconnaissance Vehicle": {
            "Penetration": None,
            "Warbond": War_Bond.URBAN_LEGENDS,
            "pack": False,
            "ID": "040113",
            "image_url": "040113.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            "Support": False,
        },
        "B-1 Supply Pack": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040114",
            "image_url": "040114.png",
            "Style": [Style.DEFAULT, Style.SPECOPS, Style.DEFAULT],
            "Support": False,
        },
        "GL-21 Grenade Launcher": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040115",
            "image_url": "040115.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
            "Support": True,
        },
        "LAS-98 Laser Cannon": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040116",
            "image_url": "040116.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            "Support": True,
        },
        "AX/LAS-5 'Guard Dog' Rover": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040117",
            "image_url": "040117.png",
            "Style": [Style.DEFAULT],
            "Support": False,
        },
        "SH-20 Ballistic Shield Backpack": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040118",
            "image_url": "040118.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            "Support": False,
        },
        "ARC-3 Arc Thrower": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040119",
            "image_url": "040119.png",
            "Style": [Style.SPECOPS, Style.DEFAULT],
            "Support": True,
        },
        "LAS-99 Quasar Cannon": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040120",
            "image_url": "040120.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
            "Support": True,
        },
        "SH-32 Shield Generator Pack": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040121",
            "image_url": "040121.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            "Support": False,
        },
        "AX/AR-23 'Guard Dog'": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "pack": True,
            "ID": "040122",
            "image_url": "040122.png",
            "Style": [Style.DEFAULT],
            "Support": False,
        },
        "EXO-45 Patriot Exosuit": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040123",
            "image_url": "040123.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            "Support": False,
        },
        "EXO-49 Emancipator Exosuit": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040124",
            "image_url": "040124.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
            "Support": False,
        },
        "TX-41 Sterilizer": {
            "Penetration": None,
            "Warbond": War_Bond.CHEMICAL_AGENTS,
            "pack": False,
            "ID": "040125",
            "image_url": "040125.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
            "Support": True,
        },
        "AX/TX-13 'Guard Dog' Dog Breath": {
            "Penetration": None,
            "Warbond": War_Bond.CHEMICAL_AGENTS,
            "pack": True,
            "ID": "040126",
            "image_url": "040126.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
            "Support": False,
        },
        "SH-51 Directional Shield": {
            "Penetration": None,
            "Warbond": War_Bond.URBAN_LEGENDS,
            "pack": True,
            "ID": "040127",
            "image_url": "040127.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            "Support": False,
        },
        "B-100 Portable Hellbomb": {
            "Penetration": Penetration.ANTI_TANK_4,
            "Warbond": War_Bond.SERVANTS_OF_FREEDOM,
            "pack": True,
            "ID": "040128",
            "image_url": "040128.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
            "Support": False,
        },
        "EAT-700 Expendable Napalm": {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.DUST_DEVILS,
            "pack": False,
            "ID": "040129",
            "image_url": "040129.png",
            "Style": [Style.EXPLOSIVE],
            "Support": False,
        },
        "MS-11 Solo Silo": {
            "Penetration": [Penetration.ANTI_TANK_3, Penetration.ANTI_TANK_5],
            "Warbond": War_Bond.DUST_DEVILS,
            "pack": False,
            "ID": "040130",
            "image_url": "040130.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
            "Support": False,
        },
        "S-11 Speargun": {
            "Penetration": [Penetration.ANTI_TANK_1, Penetration.ANTI_TANK_2, Penetration.UNARMORED_1],
            "Warbond": War_Bond.DUST_DEVILS,
            "pack": False,
            "ID": "040131",
            "image_url": "040131.png",
            "Style": [Style.SPECOPS, Style.DEFAULT],
            "Support": True,
        },
        "LIFT-182 Warp Pack": {
            "Penetration": Penetration.HEAVY,
            "Warbond": War_Bond.CONTROL_GROUP,
            "pack": True,
            "ID": "040132",
            "image_url": "040132.png",
            "Style": [Style.SPECOPS, Style.DEFAULT],
            "Support": False,
        },
        "PLAS-45 Epoch": {
            "Penetration": [Penetration.HEAVY, Penetration.ANTI_TANK_1],
            "Warbond": War_Bond.CONTROL_GROUP,
            "pack": False,
            "ID": "040133",
            "image_url": "040133.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
            "Support": True,
        },
        "AX/ARC-3 'Guard Dog' K-9": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.ANTI_TANK_3],
            "Warbond": War_Bond.FORCE_OF_LAW,
            "pack": True,
            "ID": "040134",
            "image_url": "040134.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
            "Support": False,
        },
        "GL-52 De-Escalator": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.HEAVY, Penetration.ANTI_TANK_2],
            "Warbond": War_Bond.FORCE_OF_LAW,
            "pack": False,
            "ID": "040135",
            "image_url": "040135.png",
            "Style": [Style.SPECOPS, Style.DEFAULT],
            "Support": True,
        },
        "CQC-1 One True Flag": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.MEDIUM],
            "Warbond": War_Bond.MASTERS_OF_CEREMONY,
            "pack": False,
            "ID": "040136",
            "image_url": "040136.png",
            "Style": [Style.SPECOPS, Style.DEFAULT, Style.EXPLOSIVE],
            "Support": True,
        },
        "LIFT-860 Hover Pack": {
            "Penetration": None,
            "Warbond": War_Bond.BORDERLINE_JUSTICE,
            "pack": True,
            "ID": "040137",
            "image_url": "040137.png",
            "Style": [Style.SPECOPS, Style.DEFAULT, Style.EXPLOSIVE],
            "Support": False,
        },
        "EAT-17 Expendable Anti-Tank": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "pack": False,
            "ID": "040138",
            "image_url": "040138.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS],
            "Support": False,
        },
    },

    "Red": {
        "Orbital Gatling Barrage": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 70,
            "ID": "040201",
            "image_url": "040201.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Orbital Airburst Strike": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "cooldown": 100,
            "ID": "040202",
            "image_url": "040202.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Orbital 120mm HE Barrage": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "cooldown": 180,
            "ID": "040203",
            "image_url": "040203.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Orbital 380mm HE Barrage": {
            "Penetration": "Anti-Tank IV",
            "Warbond": War_Bond.BASE,
            "cooldown": 240,
            "ID": "040204",
            "image_url": "040204.png",
            "Style": [Style.EXPLOSIVE],
        },
        "Orbital Walking Barrage": {
            "Penetration": "Anti-Tank IV",
            "Warbond": War_Bond.BASE,
            "cooldown": 240,
            "ID": "040205",
            "image_url": "040205.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Orbital Laser": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.BASE,
            "cooldown": 300,
            "ID": "040206",
            "image_url": "040206.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "Orbital Napalm Barrage": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 240,
            "ID": "040207",
            "image_url": "040207.png",
            "Style": [Style.EXPLOSIVE],
        },
        "Orbital Railcannon Strike": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "cooldown": 210,
            "ID": "040208",
            "image_url": "040208.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "Eagle Strafing Run": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040209",
            "image_url": "040209.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "Eagle Airstrike": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040210",
            "image_url": "040210.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Eagle Cluster Bomb": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040211",

            "image_url": "040211.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "Eagle Napalm Airstrike": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040212",
            "image_url": "040212.png",
            "Style": [Style.EXPLOSIVE],
        },
        "Eagle Smoke Strike": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040213",
            "image_url": "040213.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "Eagle 110mm Rocket Pods": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040214",
            "image_url": "040214.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
        },
        "Eagle 500kg Bomb": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 15,
            "ID": "040215",
            "image_url": "040215.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT, Style.SPECOPS],
        },
        "Orbital Precision Strike": {
            "Penetration": "Anti-Tank IV",
            "Warbond": War_Bond.BASE,
            "cooldown": 90,
            "ID": "040216",
            "image_url": "040216.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS],
        },
        "Orbital Gas Strike": {
            "Penetration": "Anti-Tank III",
            "Warbond": War_Bond.BASE,
            "cooldown": 75,
            "ID": "040217",
            "image_url": "040217.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
        },
        "Orbital EMS Strike": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "cooldown": 75,
            "ID": "040218",
            "image_url": "040218.png",
            "Style": [Style.SPECOPS, Style.DEFAULT],
        },
        "Orbital Smoke Strike": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "cooldown": 100,
            "ID": "040219",
            "image_url": "040219.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
    },

    "Green": {
        "E/MG-101 HMG Emplacement": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "cooldown": 180,
            "ID": "040301",
            "image_url": "040301.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "FX-12 Shield Generator Relay": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "cooldown": 90,
            "ID": "040302",
            "image_url": "040302.png",
            "Style": [Style.DEFAULT],
        },
        "A/ARC-3 Tesla Tower": {
            "Penetration": "Unarmored II",
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040303",
            "image_url": "040303.png",
            "Style": [Style.EXPLOSIVE, Style.SPECOPS, Style.DEFAULT],
        },
        "MD-6 Anti-Personnel Minefield": {
            "Penetration": "Unarmored II",
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040304",
            "image_url": "040304.png",
            "Style": [Style.EXPLOSIVE],
        },
        "MD-I4 Incendiary Mines": {
            "Penetration": Penetration.MEDIUM,
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040305",
            "image_url": "040305.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "MD-17 Anti-Tank Mines": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040306",
            "image_url": "040306.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "MD-8 Gas Mines": {
            "Penetration": None,
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040307",
            "image_url": "040307.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "A/MG-43 Machine Gun Sentry": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "cooldown": 90,
            "ID": "040308",
            "image_url": "040308.png",
            "Style": [Style.DEFAULT],
        },
        "A/G-16 Gatling Sentry": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "cooldown": 150,
            "ID": "040309",
            "image_url": "040309.png",
            "Style": [Style.DEFAULT],
        },
        "A/M-12 Mortar Sentry": {
            "Penetration": Penetration.LIGHT,
            "Warbond": War_Bond.BASE,
            "cooldown": 180,
            "ID": "040310",
            "image_url": "040310.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/AC-8 Autocannon Sentry": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 150,
            "ID": "040311",
            "image_url": "040311.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/MLS-4X Rocket Sentry": {
            "Penetration": "Anti-Tank I",
            "Warbond": War_Bond.BASE,
            "cooldown": 150,
            "ID": "040312",
            "image_url": "040312.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/M-23 EMS Mortar Sentry": {
            "Penetration": "Unarmored I",
            "Warbond": War_Bond.BASE,
            "cooldown": 180,
            "ID": "040313",
            "image_url": "040313.png",
            "Style": [Style.DEFAULT, Style.SPECOPS],
        },
        "E/AT-12 Anti-Tank Emplacement": {
            "Penetration": "Anti-Tank II",
            "Warbond": War_Bond.URBAN_LEGENDS,
            "cooldown": 180,
            "ID": "040314",
            "image_url": "040314.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/FLAM-40 Flame Sentry": {
            "Penetration": [Penetration.MEDIUM, Penetration.HEAVY],
            "Warbond": War_Bond.URBAN_LEGENDS,
            "cooldown": 150,
            "ID": "040315",
            "image_url": "040315.png",
            "Style": [Style.EXPLOSIVE, Style.DEFAULT],
        },
        "A/LAS-98 Laser Sentry": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.HEAVY],
            "Warbond": War_Bond.CONTROL_GROUP,
            "cooldown": 150,
            "ID": "040316",
            "image_url": "040316.png",
            "Style": [Style.DEFAULT],
        },
        "E/GL-21 Grenadier Battlement": {
            "Penetration": [Penetration.UNARMORED_1, Penetration.MEDIUM],
            "Warbond": War_Bond.BASE,
            "cooldown": 120,
            "ID": "040317",
            "image_url": "040317.png",
            "Style": [Style.DEFAULT, Style.EXPLOSIVE],
        },
    },
}

Armor_Passive = [
    {"Acclimated": {
        "Warbond": War_Bond.KILLZONE_CROSSOVER, 
        "ID": "050101",
        "image_url": "050101.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }},            
    {"Advance Filtration": {
        "Warbond": War_Bond.CHEMICAL_AGENTS, 
        "ID": "050102",
        "image_url": "050102.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]
        }},          
    {"Extra Padding": {
        "Warbond": War_Bond.SUPER_STORE, 
        "ID": "050103",
        "image_url": "050103.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]
        }},                    
    {"Engineering Kit": {
        "Warbond": [War_Bond.SUPER_STORE, War_Bond.DEMOCRATIC_DETONATION], 
        "ID": "050104", 
        "image_url": "050104.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
        }}, 
    {"Med-Kit": {
        "Warbond": War_Bond.SUPER_STORE, 
        "ID": "050105",
        "image_url": "050105.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},                          
    {"Scout": {
        "Warbond": [War_Bond.POLAR_PATRIOTS, War_Bond.HELLDIVERS_MOBILIZE], 
        "ID": "050106",
        "image_url": "050106.png",
        "Tag": [Style.SPECOPS]}},  
    {"Electrical Conduit": {
        "Warbond": War_Bond.CUTTING_EDGE, 
        "ID": "050107",
        "image_url": "050107.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},             
    {"Fortified": {
        "Warbond": War_Bond.SUPER_STORE,
          "ID": "050108",
          "image_url": "050108.png",
          "Tag": [Style.EXPLOSIVE]}},                        
    {"Inflammable": {
        "Warbond": War_Bond.FREEDOMS_FLAME, 
        "ID": "050109", 
        "image_url": "050109.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]}},                 
    {"Integrated Explosives": {
        "Warbond": [War_Bond.SUPER_STORE, War_Bond.SERVANTS_OF_FREEDOM], 
        "ID": "050110",
        "image_url": "050110.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},  
    {"Peak Physique": {
        "Warbond": War_Bond.VIPER_COMMANDOS, 
        "ID": "050111",
        "image_url": "050111.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},               
    {"Servo-Assisted": {
        "Warbond": War_Bond.SUPER_STORE, 
        "ID": "050112",
        "image_url": "050112.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},                   
    {"Siege-Ready": {
        "Warbond": War_Bond.URBAN_LEGENDS, 
        "ID": "050113",
        "image_url": "050113.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},                   
    {"Unflinching": {
        "Warbond": War_Bond.TRUTH_ENFORCERS, 
        "ID": "050114",
        "image_url": "050114.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},                  
    {"Desert Stormer": {
        "Warbond": War_Bond.DUST_DEVILS, 
        "ID": "050115",
        "image_url": "050115.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},
    {"Feet First": {
        "Warbond": War_Bond.ODST, 
        "ID": "050116",
        "image_url": "050116.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},
    {"Adreno-Defibrillator": {
        "Warbond": War_Bond.CONTROL_GROUP, 
        "ID": "050117",
        "image_url": "050117.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},
    {"Ballistic Padding": {
        "Warbond": War_Bond.FORCE_OF_LAW, 
        "ID": "050118",
        "image_url": "050118.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},
    {"Reinforced Epaulettes": {
        "Warbond": War_Bond.MASTERS_OF_CEREMONY,
          "ID": "050119",
          "image_url": "050119.png",
          "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},
    {"Gunslinger": {
        "Warbond": War_Bond.BORDERLINE_JUSTICE, 
        "ID": "050120",
        "image_url": "050120.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},
    {"Integrated Explosives": {
        "Warbond": War_Bond.SERVANTS_OF_FREEDOM, 
        "ID": "050121",
        "image_url": "050121.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }},
    {"Democracy Protects": {
        "Warbond": War_Bond.BASE, 
        "ID": "050122",
        "image_url": "050122.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
    }},
]

Booster = [
    {"Hellpod Space Optimization": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060101",
        "image_url": "060101.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS],
        }},  
    {"Vitality Enhancement": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060102", 
        "image_url": "060102.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]}},       
    {"UAV Recon Booster": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060103", 
        "image_url": "060103.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},           
    {"Stamina Enhancement": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060104",
        "image_url": "060104.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},         
    { "Muscle Enhancement" : {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060105",
        "image_url": "060105.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},        
    {"Increased Reinforcement Budget": {
        "Warbond": War_Bond.HELLDIVERS_MOBILIZE, 
        "ID": "060106", 
        "image_url": "060106.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }}, 
    {"Flexible Reinforcement Budget": {
        "Warbond": War_Bond.STEELED_VETERANS, 
        "ID": "060107",
        "image_url": "060107.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }},  
    {"Localization Confusion": {
        "Warbond": War_Bond.CUTTING_EDGE, 
        "ID": "060108",
        "image_url": "060108.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},             
    {"Expert Extraction Pilot": {
        "Warbond": War_Bond.DEMOCRATIC_DETONATION, 
        "ID": "060109",
        "image_url": "060109.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]}},   
    {"Motivational Shocks": {
        "Warbond": War_Bond.POLAR_PATRIOTS, 
        "ID": "060110",
        "image_url": "060110.png",
        "Tag": [Style.DEFAULT, Style.SPECOPS]
        }},              
    {"Experimental Infusion": {
        "Warbond": War_Bond.VIPER_COMMANDOS, 
        "ID": "060111",
        "image_url": "060111.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE, Style.SPECOPS]
        }},          
    {"Firebomb Hellpods": {
        "Warbond": War_Bond.FREEDOMS_FLAME, 
        "ID": "060112",
        "image_url": "060112.png",
        "Tag": [Style.DEFAULT, Style.EXPLOSIVE]
        }},               
    {"Dead Sprint": {
        "Warbond": War_Bond.TRUTH_ENFORCERS, 
        "ID": "060113",
        "image_url": "060113.png",
        "Tag": [Style.SPECOPS]}},                     
    {"Armed Resupply Pods": {
        "Warbond": War_Bond.URBAN_LEGENDS, 
        "ID": "060114",
        "image_url": "060114.png",
        "Tag": [Style.DEFAULT,Style.SPECOPS]}},
    {"Sample Extricator": {
        "Warbond": War_Bond.BORDERLINE_JUSTICE, 
        "ID": "060115",
        "image_url": "060115.png",
        "Tag": [Style.DEFAULT]
        }},
    {"Sample Scanner": {
        "Warbond": War_Bond.MASTERS_OF_CEREMONY, 
        "ID": "060116",
        "image_url": "060116.png",
        "Tag": [Style.SPECOPS]}},
    {"Stun Pods": {
        "Warbond": War_Bond.FORCE_OF_LAW, 
        "ID": "060117",
        "image_url": "060117.png",
        "Tag": [Style.SPECOPS]}},

]
