let a = [2, 1, 3, 5, 9, 2];
function firstDuplicate(a) {
  let duplicates = [];
  for (let i = 0; i < a.length; i++) {
    if (duplicates[a[i]] === undefined) {
      duplicates[a[i]] = 1;
      console.log(duplicates);
    } else {
      return a[i];
    }
  }

  //   return -1;
}
console.log(firstDuplicate(a));
