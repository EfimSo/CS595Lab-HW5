use dep::std::merkle::compute_merkle_root;
use std::hash::pedersen_hash;

fn main(
    r: Field,
    index: Field,
    path: [Field; 8],
    root: pub Field,
    id: pub Field,
) {
    let new_leaf: Field = pedersen_hash([id, r]);
    let expected_root: Field = compute_merkle_root(new_leaf, index, path);
    assert(expected_root == root);
}
