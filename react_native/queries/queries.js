import gql from "graphql-tag";

export const queries = gql`
query instrospect {
    __type(name: "Query") {
      name
      fields {
        name
        type {
          kind
          ofType {
            name
            fields {
                    name 
                  }
          }
        }
      }
    }
  }
`

