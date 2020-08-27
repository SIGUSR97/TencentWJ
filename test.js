const Fontmin = require('fontmin');

const fontmin = new Fontmin().src('fonts/*.ttc').dest('build/fonts');

fontmin.run((err, files) => {
  if (err) {
    throw err;
  }

  console.log(files[0]);
  // => { contents: <Buffer 00 01 00 ...> }
});
