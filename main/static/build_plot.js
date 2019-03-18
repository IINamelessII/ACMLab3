var margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
let svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("id", "svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.csv("http://127.0.0.1:8000/data.csv",

  // When reading the csv, I must format variables:
  function(d){
    return { xp : d.xp, yp : d.yp }
  },

  // Now I can use this dataset:
  function(data) {

    // Add X axis --> it is a date format
    var x = d3.scaleLinear()
    .domain(d3.extent(data, function(d) { return d.xp; }))
      .range([ 0, width ]);
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([d3.min(data, function(d) { return +d.yp; }), d3.max(data, function(d) { return +d.yp; })])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // Add the line
    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d.xp) })
        .y(function(d) { return y(d.yp) })
        )

})




// Building Interpolation plot
var margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
let svg1 = d3.select("#my_dataviz_i")
  .append("svg")
    .attr("id", "svg_i")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.csv("http://127.0.0.1:8000/data_interpolated.csv",

  // When reading the csv, I must format variables:
  function(d){
    return { xp : d.xp, yp : d.yp }
  },

  // Now I can use this dataset:
  function(data) {

    // Add X axis --> it is a date format
    var x = d3.scaleLinear()
    .domain(d3.extent(data, function(d) { return d.xp; }))
      .range([ 0, width ]);
    svg1.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([d3.min(data, function(d) { return +d.yp; }), d3.max(data, function(d) { return +d.yp; })])
      .range([ height, 0 ]);
    svg1.append("g")
      .call(d3.axisLeft(y));

    // Add the line
    svg1.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "red")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d.xp) })
        .y(function(d) { return y(d.yp) })
        )

})