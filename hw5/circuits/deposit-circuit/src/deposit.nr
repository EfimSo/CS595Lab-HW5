use dep::std::merkle::compute_merkle_root;
use std::hash::pedersen_hash

fn main(
    id: Field,
    r: Field,
    old_path: [Field; 8],
    old_root: pub Field,
    new_root: pub Field,
    commitment: pub Field,
    index: pub Field,
) {
    let new_leaf: Field = pedersen_hash([id, r]);
    assert(new_leaf == commitment);

    let default_leaf: Field = 0x18d85f3de6dcd78b6ffbf5d8374433a5528d8e3bf2100df0b7bb43a4c59ebd63;
    let expected_root = compute_merkle_root(default_leaf, index, old_path);
    assert(expected_root == old_root);

    let expected_new_root: Field = compute_merkle_root(new_leaf, index, new_path);
    assert(expected_new_root == new_root);

}
