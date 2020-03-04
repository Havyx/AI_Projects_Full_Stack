import React from "react";
import ReactDom from "react-dom";
// import "./index.css";

function People() {
  const friends = [
    { name: "Jone", job: "developer", age: "23", company: "Apple" },
    { name: "Jon", job: "dope", age: "43", company: "microsoft" },
    { name: "June", job: "design", age: "22", company: "ibm" }
  ];

  return (
    <section>
      <Person person={friends[0]}>
        <h1>Child</h1>
        <p>Some info about </p>
      </Person>
      <Person person={friends[1]} />
      <Person person={friends[2]} />
    </section>
  );
}

const Person = props => {
  const { name, job, age, company } = props.person;
  console.log(props);

  return (
    <article>
      <h3>{name}</h3>
      {props.children}
      <p>{job}</p>
      <p>{age}</p>
      <p>{company}</p>

      <hr />
    </article>
  );
};

ReactDom.render(<People />, document.getElementById("root"));
