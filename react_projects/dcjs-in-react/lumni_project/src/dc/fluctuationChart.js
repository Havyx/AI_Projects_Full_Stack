import React from 'react';
import * as dc from 'dc';
import {scaleLinear} from 'd3';
import {ChartTemplate} from './chartTemplate';
import {numberFormat} from './cxContext';

const fluctuationChartFunc = (divRef, ndx) => {
  const fluctuationChart = dc.barChart (divRef);
  const dimension = ndx.dimension (d => Math.round (d.close));
  const group = dimension.group ();
  fluctuationChart
    .dimension (dimension)
    .group (group)
    .gap (1)
    .width (768)
    .height (480)
    .x (scaleLinear ().domain ([12, 52]))
    .valueAccessor (x => 0 + x.value)
    .centerBar (true)
    .round (dc.round.floor)
    .renderHorizontalGridLines (true)
    .filterPrinter (filters => {
      var filter = filters[0], s = '';
      s += `${numberFormat (filter[0])}Anos ${numberFormat (filter[1])}Anos `;
      return s;
    });

  fluctuationChart.xAxis ().tickFormat (function (v) {
    return v + ' anos';
  });
  fluctuationChart.yAxis ().ticks (5);

  return fluctuationChart;
};

export const FluctuationChart = () => (
  <ChartTemplate
    chartFunction={fluctuationChartFunc}
    title="Return Distribution"
  />
);
