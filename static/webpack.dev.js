const path = require('path');
module.exports = env => {

  return {
    // watch: true,
    mode: 'development',
    devtool: 'eval',
    resolve: {
      extensions: ['.js'],
    },
    entry: {
      header : './src/header.js',
      home: './src/home.js',
      gallery: './src/page/gallery.js',
      storelist: './src/page/storelist.js',
      storedetail: './src/page/storedetail.js',
      test: './src/page/test.js',
      // health: './src/example/health.js',
      // slide: './src/example/slide.js',
      // food: './src/example/food.js',
      // profile: './src/example/profile.js',
    },
    output: {
      path: path.resolve(__dirname, 'dist'),
      publicPath: '/dist/',
      filename: '[name].js',
    },
    devServer: {
      contentBase: path.join(__dirname, 'dist'),
      publicPath: '/', // dev server root url
      hot: true,
      port: 3000,    // server port
      overlay: true, // Debug Message to Browser
      disableHostCheck: true,
      // publicPath: "/dist/", // dev server root url
    },
    module: {
      rules: [
        {
          test: [/\.css$/],
          use: ['style-loader', 'css-loader'],
        },
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader",
          }
        },
      ]
    },
  };
}