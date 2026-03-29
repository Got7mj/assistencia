<mxfile>
  <diagram name="Casos de Uso">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- ATORES -->
        <mxCell id="cliente" value="Cliente" style="shape=umlActor;" vertex="1" parent="1">
          <mxGeometry x="50" y="250" width="50" height="100" as="geometry"/>
        </mxCell>

        <mxCell id="funcionario" value="Funcionário" style="shape=umlActor;" vertex="1" parent="1">
          <mxGeometry x="900" y="250" width="50" height="100" as="geometry"/>
        </mxCell>

        <!-- CASOS DE USO -->
        <mxCell id="login" value="Realizar Login" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="400" y="50" width="160" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="manterCliente" value="Manter Cliente" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="350" y="150" width="200" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="manterFuncionario" value="Manter Funcionário" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="650" y="150" width="200" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="manterOS" value="Manter Ordem de Serviço" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="350" y="250" width="200" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="agendar" value="Agendar Visita Técnica" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="650" y="250" width="200" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="equipamento" value="Manter Equipamento" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="650" y="350" width="200" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="relatorio" value="Emitir Relatórios" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="650" y="450" width="200" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="conta" value="Registrar Conta a Receber" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="350" y="350" width="200" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="pagar" value="Pagar Conta" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="350" y="450" width="200" height="60" as="geometry"/>
        </mxCell>

        <mxCell id="consultarOS" value="Consultar OS" style="ellipse;" vertex="1" parent="1">
          <mxGeometry x="150" y="350" width="180" height="60" as="geometry"/>
        </mxCell>

        <!-- RELAÇÕES -->
        <!-- Cliente -->
        <mxCell id="c1" style="endArrow=none;" edge="1" parent="1" source="cliente" target="login"/>
        <mxCell id="c2" style="endArrow=none;" edge="1" parent="1" source="cliente" target="consultarOS"/>
        <mxCell id="c3" style="endArrow=none;" edge="1" parent="1" source="cliente" target="pagar"/>

        <!-- Funcionário -->
        <mxCell id="f1" style="endArrow=none;" edge="1" parent="1" source="funcionario" target="login"/>
        <mxCell id="f2" style="endArrow=none;" edge="1" parent="1" source="funcionario" target="manterCliente"/>
        <mxCell id="f3" style="endArrow=none;" edge="1" parent="1" source="funcionario" target="manterFuncionario"/>
        <mxCell id="f4" style="endArrow=none;" edge="1" parent="1" source="funcionario" target="manterOS"/>
        <mxCell id="f5" style="endArrow=none;" edge="1" parent="1" source="funcionario" target="agendar"/>
        <mxCell id="f6" style="endArrow=none;" edge="1" parent="1" source="funcionario" target="equipamento"/>
        <mxCell id="f7" style="endArrow=none;" edge="1" parent="1" source="funcionario" target="relatorio"/>

        <!-- INCLUDE -->
        <mxCell id="i1" value="<<include>>" style="dashed=1;endArrow=open;" edge="1" parent="1" source="manterOS" target="conta"/>

        <mxCell id="i2" value="<<include>>" style="dashed=1;endArrow=open;" edge="1" parent="1" source="pagar" target="consultarOS"/>

        <!-- EXTEND -->
        <mxCell id="e1" value="<<extend>>" style="dashed=1;endArrow=open;" edge="1" parent="1" source="agendar" target="manterOS"/>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
