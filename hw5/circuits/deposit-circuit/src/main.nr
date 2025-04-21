use dep::std::merkle::compute_merkle_root;
use std::hash::pedersen_hash;

fn main(
    id: Field,
    r: Field,
    oldPath: [Field; 8],
    oldRoot: pub Field,
    newRoot: pub Field,
    commitment: pub Field,
    index: pub Field,
) {
    let new_leaf: Field = pedersen_hash([id, r]);
    assert(new_leaf == commitment);

    let default_leaf: Field = 0x18d85f3de6dcd78b6ffbf5d8374433a5528d8e3bf2100df0b7bb43a4c59ebd63;
    let expected_root = compute_merkle_root(default_leaf, index, oldPath);
    assert(expected_root == oldRoot);

    let expected_newRoot: Field = compute_merkle_root(new_leaf, index, oldPath);
    assert(expected_newRoot == newRoot);

}
