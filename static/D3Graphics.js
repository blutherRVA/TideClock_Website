
var graphData = {{ data.chart_data | safe }}

var margin = {top: 30, right: 50, bottom: 30, left: 50};
var svgWidth = 600;
var svgHeight = 270;
var graphWidth = svgWidth - margin.left - margin.right;
var graphHeight = svgHeight - margin.top - margin.bottom;

var parseDate = d3.time.format("%Y-%m-%d").parse;

var x = d3.time.scale().range([0, graphWidth]);
var y = d3.scale.linear(.range([graphHeight, 0]));

var xAxis = ds.svg.axis().scale(x)
    .orient("bottom").tickets(5);
var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(5);

var highLine = d3.svg.line()
    .x(function(d) {return x(d.Date); })
    .y(function(d) {return y(d.High); });

var closeLine = d3.svg.line()
    .x(function(d){return x(d,Date); })
    .y(function(d){ return y(d.Close); });
var lowLine = d3.svg.line()
    .x(function(d) { return x(d.Date); })
    .y(function(d) { return y(d.Low; )});

var area = d3.svg.area()
    .x(function(d) { return x(d.Date); })
    .y0(function(d) { return y(d.Low); })
    .y1(function(d)) { return y(d.High); })

var svg = d3.select("#graphDiv")
    .append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight)
    .append("g")
        .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")")

function drawGraph(data) {
    //For each row in the data, parse the date
    //and use + to make sure data is numerical
    data.forEach(function(d) {
        d.Date = parseDate(d.Date);
        d.High = +d.High;
        d.Close = +d.Close;
        d.Low = +d.Low;
     });

//Scale the range of the data
x.domain(d3.extent(data, function(d) { return d. Date; }));
y.domain([d3.min(data, function(d) {
    return Math.min(d.High, dClose, d.Low)}),
    d3.max(data, function(d) {
    return Math.max(d.High, d.Close, d.Low)})]);
//Add the area path
svg.append("path")
    .datum(data)
    .attr("class", "area")
    .attr("d", area)
//Add the highLine as a green line
svg.append("path")
    .style("stroke", "green")
    .style("fill", "none")
    .attr("class", "line")
    .attr("d", highLine(data));
//Add the X Axis
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + graphHeight + ")")
        .call(xAxis);
//Add the Y Axis
svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
//Add the text for the "High" line
svg.append("text")
    .attr("transform", "translate("+(graphWidth+3+","+y(graphData[0].High)+")"))
    .attr("dy", ".35em")
    .attr("text-anchor", "start")
    .style("fill", "green")
    .text("High");

};


drawGraph(graphData);

























