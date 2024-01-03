from itertools import combinations

M = int(input())
meeting_masks = [set(meeting_subset) for meeting_subset in combinations(range(M), M//2)]

print(len(meeting_masks))
for m in range(M):
    members = list(
        i+1
        for i, meeting_mask in enumerate(meeting_masks)
        if m in meeting_mask
    )
    print(len(members))
    print(*members)

    response = input()
