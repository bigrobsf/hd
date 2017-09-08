/* jshint esversion: 6 */
/* jshint jquery: true */
/* jshint devel: true */
/* jshint node: true */
/* jshint browser: true */
'use strict';

$(function() {

  $('#chart').on('click', () => {

    $('#chart').remove();

    var userId = $('p.hidden').text();

    $.getJSON(`/reports/${userId}/graph`).then(data => {

      var svg = d3.select("svg"),
          margin = {top: 20, right: 40, bottom: 70, left: 20},
          width = +svg.attr("width") - margin.left - margin.right,
          height = +svg.attr("height") - margin.top - margin.bottom;

          var x = d3.scaleBand()
                    .rangeRound([0, width]).padding(0.1);

          var y = d3.scaleLinear()
                    .rangeRound([height, 0]);

          var g = svg.append("g")
                     .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        data.forEach(function(d) {
            d.date = d.date;
            d.length = +d.length;
            d.sum = +d.sum;
        });

        x.domain(data.map(function(d) { return d.date; }));
        y.domain([0, d3.max(data, function(d) { return d.sum; })]).nice();

        g.append("g")
            .attr("class", "axis axis--x")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x))
            .selectAll("text")
                .style("text-anchor", "end")
                .attr("dx", "-.8em")
                .attr("dy", ".15em")
                .attr("transform", "rotate(-65)");

        g.append("g")
            .attr("class", "axis--y")
            .attr("transform", "translate(" + width + ", 0)")
            .call(d3.axisRight(y).ticks())
          .append("text")
            .attr("x", -80)
            .attr("y", y(y.ticks().pop()) + 0.5)
            .attr("dy", "0.5em")
            .attr("fill", "#000")
            .attr("font-weight", "bold")
            .attr("text-anchor", "start")
            .text("Total Weight");

        g.selectAll(".bar")
          .data(data)
          .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function(d) { return x(d.date); })
            .attr("y", function(d) { return y(d.sum); })
            .attr("width", x.bandwidth())
            .attr("height", 0)
            .on("mousemove", showTooltip)
            .on("touchstart", showTooltip)
            .on("mouseout", function() {
              d3.select(".tooltip")
              .style("opacity", 0);
            })
            .attr("height", function(d) { return height - y(d.sum); });

        svg
          .append("text")
            .text("Total Weight by Workout")
            .attr("x", width / 2)
            .attr("y", 20)
            .style("text-anchor", "middle")
            .style("font-size", "16px")
            .style("font-weight", "bold");

            function showTooltip(d) {
              d3.select(".tooltip")
                  .style("opacity", 1)
                  .style("top", d3.event.y + 20 + "px")
                  .style("left", d3.event.x - 20 + "px")
                  .html(`
                    <p>Duration: ${d.length} minutes</p>
                  `);
            }

    });
  });
});
