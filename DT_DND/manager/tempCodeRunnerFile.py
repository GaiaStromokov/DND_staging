                for level in range(1, 10):
                    if level in db.Spell["Slot"]:
                        db.Spell["Slot"][level] = [False] * len(db.Spell["Slot"][level])