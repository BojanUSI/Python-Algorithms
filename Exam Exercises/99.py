def bst_range_weight(t, k1, k2):
    if t == None:
        return 0
    
    if t.key == k1 and t.key == k2:
        return 1
    

    if t.key < k2 and t.key > k1:
        return 1 + bst_range_weight(t.left, k1, k2) + \
            bst_range_weight(t.right, k1, k2)
    
    if t.key <= k1:
        return bst_range_weight(t.right, k1, k2)
    
    else:
        return bst_range_weight(t.left, k1, k2)