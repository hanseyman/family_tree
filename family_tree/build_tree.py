drew = FamilyTree("Drew", "Hanson", "E.", mother="Janis", father="Dwight", comments="This is me")
janis = FamilyTree("Janis", "Price", "Carol", child=drew, mother="Pat", father="Jim", comments="this is mom")
dwight = FamilyTree("Dwight", "Hanson", "Eugene", child=drew, comments="this is dad")
pat = FamilyTree("Pat", "Price", "The Killer", child=janis, comments="this is Granna")
byron = FamilyTree("Byron", "Hanson", child=dwight, comments="This is dad's dad")
ailene = FamilyTree("Ailene", "Hanson", child=dwight, comments="This is dad's mom")

drew.father = dwight
drew.mother = janis

drew.PrintAll()