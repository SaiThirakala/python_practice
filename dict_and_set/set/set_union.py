# New set with all unique items that are present in both sets
# Can create union with either `|` or union function
# all_animals_1 = farm_animals.union(wild_animals)
# all_animals_2 = farm_animals | wild_animals
# print(all_animals_1)
# print(all_animals_2)
#
# print()
# # Set union is commutative
# all_animals_3 = wild_animals.union(farm_animals)
# print(all_animals_1)
# print(all_animals_3)

from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#     # Create a new set each time loop iterates
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction
#
#     # Update the existing set instead of creating a new one
#     # meds_to_watch.update(interaction)
#     meds_to_watch |= interaction

meds_to_watch.update(*adverse_interactions)
print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep="\n")

