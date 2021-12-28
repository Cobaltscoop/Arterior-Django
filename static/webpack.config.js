const path = require('path');
module.exports = env => {

  return {
    mode: 'production',
    devtool: 'hidden-source-map', 
    resolve: {
      extensions: ['.js'],
    },
    entry: {
      header : './src/header.js',
      home: './src/home.js',
      gallery: './src/page/gallery.js',
      storelist: './src/page/storelist.js',
      storedetail: './src/page/storedetail.js',
    },
    output: {
      path: path.resolve(__dirname, 'dist'),
      publicPath: '/dist/',
      filename: '[name].js',
    },
    module: {
      rules: [
        {
          test: [/\.css$/],
          use: ['style-loader', 'css-loader'],
        },
      ]
    },
  };
}