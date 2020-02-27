import React from "react";
import { BubbleChart } from "./bubbleChart";
import { GainOrLossChart } from "./gainOrLessChart";
import { QuarterChart } from "./quarterChart";
import { DayOfWeekChart } from "./dayOfWeekChart";
import { FluctuationChart } from "./fluctuationChart";
import { MoveChart } from "./moveChart";
import { DataTable } from "./nasdaqTable";
import { DataContext } from "./cxContext";

export const Dashboard = props => {
  return (
    <DataContext>
      <BubbleChart />

      <MoveChart />

      <GainOrLossChart />

      <FluctuationChart />

      <QuarterChart />

      <DayOfWeekChart />

      <DataTable />
    </DataContext>
  );
};
